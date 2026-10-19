---
title: How should Dutch technical SMEs assess AI suppliers?
status: APPROVED
---
<!-- published-by: publish_wiki.py -->

# How should Dutch technical SMEs assess AI suppliers?

!!! warning "Overall confidence: MEDIUM"
    Approved by **Kyran Weijman** on 2026-10-19.
    Research last updated 2026-10-05.


## Research question
How should Dutch technical SMEs assess AI suppliers?

## Business relevance
Waterkracht B.V. and similar Dutch technical SMEs (equipment design, assembly, sales, service) increasingly buy AI-based tools from outside suppliers (e.g. predictive maintenance, quality inspection, planning software) rather than building AI in-house. Choosing the wrong supplier can mean unreliable results, legal exposure, or wasted budget the company cannot easily recover. A simple, low-cost way to check a supplier before signing a contract is directly useful to an SME owner with no in-house AI or legal team.

## Key findings
- Two Dutch methodologies were evaluated: the ECP "Artificial Intelligence Impact Assessment" (2018) and the Rijksoverheid "AI Impact Assessment 2.0" (December 2024). Both are **self-assessment tools for organisations deploying AI**, not supplier-vetting checklists. Neither gives a ready-made list of criteria for comparing AI suppliers.
- The ECP tool states that "the provider and producer of the AI solution must ensure that a number of technical preconditions are met (for example, integrity of data, safety and continuity), but must also offer facilities allowing the organisation deploying the AI to take responsibility and to be transparent about the consequences." This is the only direct statement found on what a buyer should expect from a supplier. The tool also notes it "can also be used by developers of AI to test applications," meaning an SME could in principle ask a supplier to run through it too.
- The Rijksoverheid AI Impact Assessment 2.0 touches supplier questions only briefly: it asks, when a system is built by an external party, "what are the contractual arrangements?" It also lists an Annex 2, "Questions for developers (providers) of high-risk AI systems," but the content of that annex was not available in the material reviewed, so its actual questions are not stated here.
- The Rijksoverheid tool is built around the finalised EU AI Act risk categories (Regulation (EU) 2024/1689) (unchecked against primary legal text). This makes it more current than the 2018 ECP tool, which predates the AI Act entirely.
- Both tools assume a multidisciplinary project team (e.g. CIO, CISO, legal, privacy, ethics advisor for the government tool). Not stated whether either tool offers a lighter version for a small company without these roles. This is a real feasibility gap for an SME: most technical SMEs do not have a privacy officer or in-house jurist.
- No source reviewed gives concrete, ready-to-use supplier-comparison criteria (price, contract terms, data ownership, technical due diligence, vendor lock-in, support/SLA). Not stated in either source.

## Risks
- Relying only on these two tools could give a false sense of thoroughness: they assess *whether to use AI responsibly inside your own organisation*, not *whether this particular supplier is trustworthy*.
- The ECP tool is from 2018 and does not address the EU AI Act, generative AI, or current supplier-risk practices (unchecked against primary legal text).
- If an SME signs a contract with an AI supplier without confirming data integrity, safety, continuity and transparency arrangements (as the ECP document flags), it may unknowingly take on legal or operational responsibility that the supplier should share (unchecked against primary legal text).
- The AI Act risk-category framing in the 2024 Rijksoverheid tool may apply differently depending on whether the SME is the "deployer" or the supplier is the "provider" under the Act; this distinction carries legal obligations (unchecked against primary legal text). Not stated in detail in the material reviewed.
- Using a government or multi-stakeholder tool built for large organisations "as-is" may overwhelm a small team and cause the assessment to be skipped altogether.

## Checklist
For a technical SME owner evaluating an AI supplier, based only on what the sources state:
1. Ask the supplier directly how they ensure data integrity, safety and continuity of the AI solution (per ECP, 2018).
2. Ask the supplier what facilities they offer so your company can take responsibility and be transparent about the AI's consequences (per ECP, 2018).
3. If the system is built or hosted by an external party, get the contractual arrangements in writing before go-live (per Rijksoverheid AI Impact Assessment 2.0, Dec 2024).
4. Check whether the supplier is a "provider" under the EU AI Act and what risk category the system falls into; confirm this with legal advice, not with this handbook (unchecked against primary legal text).
5. Do not assume either tool reviewed here gives a complete supplier checklist — treat both as a starting point only.

## Next action
Ask your IT or operations lead to request, in writing, the data-integrity, safety, continuity and transparency arrangements from each AI supplier under consideration, before any contract is signed.

## Source list with confidence
- Artificial Intelligence Impact Assessment (English version), ECP | Platform for the Information Society, 2018 - https://ecp.nl/wp-content/uploads/2019/01/Artificial-Intelligence-Impact-Assessment-English.pdf - Confidence: MEDIUM
- AI Impact Assessment 2.0: Het hulpmiddel voor een betrouwbaar AI-project (version 2.0, December 2024), Ministry of Infrastructure and Water Management (Rijksoverheid/IenW) - rijksoverheid.nl (binaries path as given in evaluation) - Confidence: MEDIUM
