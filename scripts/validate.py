#!/usr/bin/env python3
"""CBP syntax gateway. Does not establish the truth of any claim."""
from __future__ import annotations
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT=Path(__file__).resolve().parent.parent
FAKE_HOSTS={'example.com','www.example.com','example.org','www.example.org','example.net','www.example.net'}


def load_json(path:Path):
    return json.loads(path.read_text(encoding='utf-8'))


def issues_for(instance:dict,schema:dict):
    validator=Draft202012Validator(schema,format_checker=FormatChecker())
    return [f"{'.'.join(map(str,e.absolute_path)) or '<root>'}: {e.message}" for e in sorted(validator.iter_errors(instance),key=lambda e:list(map(str,e.absolute_path)))]


def validate_contribution(path:Path,schema:dict,known_ids:set[str],live:bool=True)->list[str]:
    try: data=load_json(path)
    except Exception as exc: return [f'Unable to parse JSON: {exc}']
    errs=issues_for(data,schema)
    if errs: return errs
    if data['challenge_id'] not in known_ids:
        errs.append('Unknown challenge_id; no matching authoritative manifest.')
    if live:
        raw=path.read_text(encoding='utf-8').lower()
        if '[synthetic test' in raw or re.search(r'https://(?:www\.)?example\.(?:com|org|net)\b',raw):
            errs.append('Synthetic or example.com test evidence cannot be used in live submissions.')
    return errs


def check_pr_changes(base_sha:str,repo_root:Path)->list[str]:
    cmd=['git','diff','--name-only',f'{base_sha}...HEAD']
    proc=subprocess.run(cmd,cwd=repo_root,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    if proc.returncode: return [f'Unable to inspect changed files: {proc.stderr.strip()}']
    paths=[x for x in proc.stdout.splitlines() if x.strip()]
    if not paths: return ['Pull request contains no file changes.']
    return [f'PRs may only add or edit JSON files in submissions/: {path}' for path in paths if not(re.fullmatch(r'submissions/[A-Za-z0-9_-]+\.json',path))]


def validate_repository(repo_root:Path)->tuple[list[str],int]:
    errors=[]
    challenge_schema=load_json(repo_root/'schemas/challenge.schema.json')
    contribution_schema=load_json(repo_root/'schemas/contribution.schema.json')
    Draft202012Validator.check_schema(challenge_schema)
    Draft202012Validator.check_schema(contribution_schema)
    manifests=sorted((repo_root/'challenges').glob('*.manifest.json'))
    if not manifests: errors.append('No challenge manifests found.')
    known=set()
    for path in manifests:
        try:
            data=load_json(path)
            errors += [f'{path.relative_to(repo_root)}: {x}' for x in issues_for(data,challenge_schema)]
            if data.get('challenge_id'):
                known.add(data['challenge_id'])
                if path.stem != data['challenge_id']+'.manifest': errors.append(f'Challenge ID and filename disagree: {path.name}')
        except Exception as exc: errors.append(f'{path}: {exc}')
    submissions=sorted((repo_root/'submissions').glob('*.json'))
    ids=set()
    for path in submissions:
        e=validate_contribution(path,contribution_schema,known,live=True)
        errors.extend([f'{path.relative_to(repo_root)}: {item}' for item in e])
        try:
            sub_id=load_json(path).get('submission_id')
            if sub_id in ids: errors.append(f'Duplicate submission_id: {sub_id}')
            ids.add(sub_id)
        except Exception: pass
    return errors,len(submissions)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--check-pr-base',help='Only JSON submissions may be changed in a public PR.')
    args=parser.parse_args()
    if args.check_pr_base:
        errs=check_pr_changes(args.check_pr_base,ROOT)
        if errs:
            for e in errs: print('ERROR:',e,file=sys.stderr)
            return 1
        print('PASS: PR changes limited to submissions/ JSON.')
        return 0
    errors,n=validate_repository(ROOT)
    if errors:
        for e in errors: print('ERROR:',e,file=sys.stderr)
        return 1
    print(f'PASS: challenge manifests and {n} live submission(s) are schema-valid. This is NOT factual verification.')
    return 0

if __name__=='__main__': sys.exit(main())
