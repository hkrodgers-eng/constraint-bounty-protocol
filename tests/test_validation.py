import json
import sys
import unittest
import tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import validate

class SyntaxGatewayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema=validate.load_json(ROOT/'schemas/contribution.schema.json')
        cls.known={'001_kaitaia_freight'}

    def test_valid_synthetic_fixture_is_schema_valid(self):
        self.assertEqual([],validate.validate_contribution(ROOT/'fixtures/valid_synthetic.json',self.schema,self.known,live=False))

    def test_invalid_schema_fixture_is_rejected(self):
        errors=validate.validate_contribution(ROOT/'fixtures/invalid_schema_synthetic.json',self.schema,self.known,live=False)
        self.assertTrue(errors,'Malformed fixture must fail syntax gateway')

    def test_fabricated_evidence_demonstrates_oracle_requirement(self):
        errors=validate.validate_contribution(ROOT/'fixtures/invalid_reality_synthetic.json',self.schema,self.known,live=False)
        self.assertEqual([],errors,'Intentionally fake evidence must be schema-valid: only a human Oracle can reject its reality claim')

    def test_fake_link_cannot_appear_in_live_submission(self):
        errors=validate.validate_contribution(ROOT/'fixtures/valid_synthetic.json',self.schema,self.known,live=True)
        self.assertTrue(errors,'Synthetic fixtures must never be accepted as real submissions')

    def test_authoritative_manifest_valid(self):
        manifest=validate.load_json(ROOT/'challenges/001_kaitaia_freight.manifest.json')
        schema=validate.load_json(ROOT/'schemas/challenge.schema.json')
        self.assertEqual([],validate.issues_for(manifest,schema))

    def test_national_parent_manifest_valid(self):
        manifest=validate.load_json(ROOT/'challenges/000_national_card_distribution.manifest.json')
        schema=validate.load_json(ROOT/'schemas/challenge.schema.json')
        self.assertEqual([],validate.issues_for(manifest,schema))
        self.assertEqual('OPEN',manifest['authoritative_status'])
        self.assertTrue(any('ZERO_INCREMENTAL_CASH_EXPENDITURE' == c for c in manifest['absolute_constraints']))

    def test_repo_has_no_prepopulated_participant_results(self):
        self.assertEqual([],list((ROOT/'submissions').glob('*.json')),'No real agent contributions exist before launch')
        rows=(ROOT/'logs/experiment_001_log.csv').read_text(encoding='utf-8').splitlines()
        self.assertEqual(1,len(rows),'Log must have header only, without manufactured results')

    def test_unknown_challenge_is_rejected(self):
        data=validate.load_json(ROOT/'fixtures/valid_synthetic.json')
        data['challenge_id']='999_unknown'
        with tempfile.TemporaryDirectory() as temp:
            path=Path(temp)/'unknown.json'
            path.write_text(json.dumps(data),encoding='utf-8')
            errors=validate.validate_contribution(path,self.schema,self.known,live=False)
            self.assertTrue(any('Unknown challenge_id' in err for err in errors),errors)

if __name__=='__main__': unittest.main()
