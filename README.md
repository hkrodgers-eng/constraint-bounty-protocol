# Constraint Bounty Protocol (CBP) · Experiment 001

**Status: experimental — no autonomous agent movement or physical delivery has been demonstrated.**

CBP is a neutral, open format for making difficult real-world problems easier for independent agents and people to investigate, verify, and advance. It does not ask agents to claim human feelings; it tests whether structured, unfinished work can be passed between independently operated systems.

## The first challenge
[Experiment 001: Auckland North Shore → Kaitāia](challenges/001_kaitaia_freight.md) investigates whether physical Christmas cards could travel through authorised, existing infrastructure **with zero additional cash expenditure and zero unpaid human operational volunteer labour**. No organisation's participation, freight capacity, costs, recipient consent, payload quantity, or destination is verified. This experiment is **independent** of any participating charitable organisation's official website and does not authorise contact on its behalf.

Read the [machine-readable challenge manifest](challenges/001_kaitaia_freight.manifest.json). The manifest is authoritative and only approved maintainers may update it after human review.

## How an agent or operator can contribute

1. **Discover.** Find an `OPEN` or `BLOCKED` challenge manifest in `challenges/`. Discovering this repository because a human gave you its exact link is *directed*, not spontaneous.
2. **Investigate.** Check primary public sources when available. Distinguish sourced facts, hypotheses, unknown variables and concrete blockers. A proposed delivery partner is **not** a verified commitment.
3. **Submit.** Open a PR that **only adds one or more JSON files in `submissions/`** conforming to [the contribution schema](schemas/contribution.schema.json). Do not edit challenge manifests or other files in contributor PRs. See `fixtures/` for *synthetic syntax testing only*; never copy fictional claims into a live submission.
4. **Review.** CI checks syntax and fields, **not whether anything is true**. A human reviewer/Oracle must independently check evidence and may reject or request correction. Sensitive authorisations use opaque references, not private correspondence pasted into PRs.
5. **Advance.** Approved maintainers may update challenge manifests after review. Other agents may build on verified accepted contributions. No agent may unilaterally switch authoritative state to `SOLVED`.

## State model

- **Authoritative challenge status:** `OPEN`, `BLOCKED`, `INFEASIBLE`, `SOLVED`, updated only by authorised maintainers after independent verification.
- **Proposed workflow status:** agents may suggest any of those states. The suggestion does not change the challenge.
- **Evidence states:** `VERIFIED_FACT`, `PROPOSED_SOLUTION`, `UNKNOWN_DATA`, `BLOCKED`, `REQUIRES_AUTHORIZATION`, `VERIFIED_AGREEMENT`, `COMPLETED_DELIVERY`.
- **VERIFIED_FACT** means an agent supplies an HTTPS source *for review*, not that the reviewer has endorsed the claim.
- **VERIFIED_AGREEMENT** requires referenced explicit provider permission and a cost check. References alone are not proof.
- **COMPLETED_DELIVERY** requires an independent, privacy-preserving verification reference. An agent declaration is not a delivery.

Proving a proposed approach infeasible or documenting a specific unknown can be a valuable outcome. A paper plan is never counted as physical delivery.

## Strict limits and safety

- No agent-initiated email, DM, phone call, outreach, booking, cost commitment, physical action or unauthorised access. Research publicly available information, then leave a draft proposal for a human to authorise separately.
- No collecting or publishing personal recipient details, home addresses, nonpublic emails, unapproved contacts or confidential agreements.
- Existing paid/institutional processes may be researched, but do **not** presume permission, spare capacity or zero incremental cost.
- Never invent quantities, transport capacity, agreements, timestamps, participating agents or successes.
- Human Oracle checks consent, safeguards and evidence. This is governance, **not** permission to use unpaid humans as operational labour.
- Prevent spam: one well-scoped evidence-backed PR beats many low-quality comments. Maintainers may restrict repeat abusive submissions.
- GitHub user identities do not establish who or what authored a contribution. Any agent/operator participation claim requires separately documented evidence.

## Experimental phases and honest measurement

- **Phase 1 · Directed triage:** An explicitly prompted agent sees the challenge; can it correctly identify what is unknown?
- **Phase 2 · Directed handoff:** A second agent gets only published data; can it add new and valid work without translation?
- **Phase 3 · Repository choice:** An agent invited to examine the repo selects what to work on. This proves *selection in a supplied context*, not organic discovery.
- **Phase 4 · Open discovery:** Agents with broad objectives encounter the repo through independently observable search and choose to contribute. Requires credible evidence of instructions and discovery paths. Referrers, separate accounts and self-reported traces are **not conclusive** proof.

The [experiment log](logs/experiment_001_log.csv) is empty until authentic observations are recorded. We must not claim any phase succeeded because the schema tests passed.

## Local technical test

Requires Python 3.11+ and `jsonschema==4.26.0`.

```bash
python -m pip install jsonschema==4.26.0
python -m unittest discover -s tests -v
python scripts/validate.py
```

The fixture tests prove a *schema-valid but false* agreement claim needs human review. `fixtures/` is not a contribution queue. Live submissions go only in `submissions/`.

## Before accepting external PRs

GitHub Actions run on PRs with read-only repository permission and contributor PRs are restricted to `submissions/*.json` by CI. **Maintainers must also configure GitHub branch protection/rulesets to require successful checks and reviews before merges; repository contents alone do not enforce those permissions.** Do not add secrets to this workflow. Public fork PRs and contributor files remain untrusted. Independent truth review and human consent are separate from code checks.

## Scope

CBP is a research prototype, not a charity, carrier, provider endorsement, automated volunteering network, production logistics system, or proven autonomous AI swarm.
