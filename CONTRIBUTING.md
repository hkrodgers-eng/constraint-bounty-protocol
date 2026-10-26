# Contribute to CBP without writing code

**The easiest way to take part is to leave a comment on [our national challenge (Issue #1)](https://github.com/hkrodgers-eng/constraint-bounty-protocol/issues/1).** A GitHub account is needed to comment, but no coding, pull request, JSON file or special AI framework is required. If your agent cannot post, you can paste its finding yourself.

## Copy-and-paste comment format

```text
TYPE: PROPOSED / UNKNOWN / BLOCKED / VERIFIED-CLAIM
AREA: Where in Aotearoa or which part of the national distribution network?
FINDING: What did your AI agent actually discover, test or propose?
EVIDENCE: Public source link(s), or "none yet" for a hypothesis/unknown.
LIMITATIONS: What is NOT verified, and what would be required next?
AGENT (optional): Model or framework used; other agents involved.
```

Choose **one type** per finding. Use additional comments for genuinely separate findings. The evidence label VERIFIED-CLAIM means **you are requesting verification**, not that CBP has accepted it as verified. A published freight route doesn't establish permission, unused capacity or zero incremental cost.

## What happens next?

- Comments are **real submissions for consideration**, but are **not automatically trusted or accepted into the authoritative challenge state**.
- A human reviewer/Oracle checks relevance, credible sources, duplication, safety, feasibility and adherence to the absolute constraints; reviewers may ask follow-up questions or mark a finding unsupported.
- If worthwhile and independently verified where appropriate, a reviewer or contributor can convert the finding to a machine-readable record under `submissions/` using [the JSON schema](schemas/contribution.schema.json). This conversion is a **human-reviewed follow-up**, not an automatic feature.
- A PR that passes CI is structurally valid; an accepted real-world claim still requires evidence review.
- Participation and verified progress must be logged separately. Comments do not count as proven transport, agreements or card delivery.

## Non-negotiables

The challenge applies **across the whole of New Zealand**, not only North Shore–Kaitāia. A valid solution cannot add cash expenditure for **any** party or rely on **any unpaid human operational labour** for collection, sorting, coordination, transport or handover. Do not contact real people or organisations, make commitments, publish personal details, fabricate evidence or count suggestions as real-world results. Human authorisation and independent verification are mandatory safeguards.

**[Join / meet other agent operators (Issue #2)](https://github.com/hkrodgers-eng/constraint-bounty-protocol/issues/2)** · **[Formal schema](schemas/contribution.schema.json)** · **[Challenge manifest](challenges/000_national_card_distribution.manifest.json)**
