---
title: What are use cases for AI in the sector that the company Waterkracht is in?
status: APPROVED
---
<!-- published-by: publish_wiki.py -->

# What are use cases for AI in the sector that the company Waterkracht is in?

!!! danger "Overall confidence: LOW"
    Approved by **Kyran Weijman** on 2026-10-19.
    Research last updated 2026-10-09.


## AI Use Cases for Waterkracht B.V. (Industrial Equipment Sector)

## Research question
What are use cases for AI in the sector that the company Waterkracht is in?

## Business relevance
Waterkracht designs, assembles, sells and services industrial equipment. AI could help in two ways: making the equipment itself smarter, and making internal work (planning, quotes, service) faster. Before spending money or time, the owner needs a realistic picture of what is proven, what is vendor marketing, and what is still untested for a company of Waterkracht's size.

## Key findings

1. **Predictive maintenance for pumps and other equipment.** Several sources describe using sensor data (temperature, flow, pressure, vibration) and machine learning to predict equipment failure before it happens.
   - A 2023 trade-magazine article describes two vendor case studies: a power-plant pump and an offshore oil & gas pump installation, where machine learning reportedly gave 1-5 days of early warning and avoided large losses. These examples use large-scale sensor networks (one case used over 30,000 sensor points) and are not shown to be realistic for an SME's scale or budget.
   - A 2025 academic preprint built a predictive model for centrifugal pumps using time-series data. Results were moderate and got worse the further ahead the model tried to predict (about 69% detection rate at 5 minutes, dropping to about 49% at 30 minutes). This is an unreviewed preprint, so the results are not independently confirmed.
   - A Dutch smart-manufacturing platform (Smart Industry NL) also lists predictive maintenance as a realistic starting point for manufacturers, stating it can be done "without large budgets, without data scientists" - but gives no evidence or cost figures to back this claim.

2. **Computer vision for quality control.** The same Smart Industry NL page describes using cameras and AI to catch product defects that people miss. No cost, accuracy data, or case study is given.

3. **AI-assisted production planning.** Smart Industry NL also mentions AI that helps plan production based on orders, capacity and material availability. Again, no implementation detail or evidence is given.

4. **Generative AI for office tasks.** Smart Industry NL lists generative AI for drafting quotes, answering technical questions, and helping write software. This is presented as a low-cost, low-effort entry point, but without supporting evidence.

5. **Sector-level framing from the industry association FME.** FME (the Dutch trade association for machine-building companies) describes AI and data technology in general terms as a way to work "more effectively and efficiently" ("effectiever en efficiënter") and make products "smarter" ("slimmer"). It names manufacturing, logistics, chemistry and robotics as sectors with potential, which overlaps with Waterkracht's field. However, this is promotional text about FME's own programs, not a list of concrete use cases.

6. **Two intended sources could not be used.** A government report on AI use among Dutch SMEs ("Onderzoek AI-gebruik in het mkb: Ambitie of aarzeling?") and one other PDF source could not be read in usable text form. No findings from these could be extracted or checked. They should be re-attempted before being relied on.

## Risks

- Most concrete case studies found (power plant, offshore platform) are large-scale operations, not representative of an SME. Applying their results to Waterkracht without testing is risky.
- The pump-maintenance trade article is written by a vendor selling that exact technology, so its savings figures and performance claims are self-reported and not independently checked.
- The academic preprint is not yet peer-reviewed, and its accuracy drops the further ahead it tries to predict - it is not a ready-to-use product.
- The two most "official"-sounding sources (FME, Smart Industry NL) describe benefits in general terms but give no cost, data requirement, or implementation detail suited to a small company.
- One government source could not be read at all; its content, author, and date remain unconfirmed.
- No source in this review discussed data protection or other legal obligations relevant to collecting sensor or customer data; if Waterkracht moves forward, legal requirements around data handling would need separate, direct legal review (unchecked against primary legal text).
- No instruction-like or manipulative content was found in any of the fetched sources; all read as ordinary web/academic/magazine content.

## Checklist
Before starting any AI pilot, Waterkracht should check:
- [ ] Do we already collect sensor data (temperature, pressure, flow, vibration) from equipment we service or sell? If not, predictive maintenance is not yet feasible.
- [ ] Do we have historical records of past equipment failures to train or test a model against?
- [ ] Is there a specific, recurring problem (e.g. repeat pump failures, slow quoting) worth solving, rather than "AI" as a goal in itself?
- [ ] Have we asked at least one independent (non-vendor) expert or peer company about real-world cost and effort for a similar pilot?
- [ ] Do we understand what customer or sensor data would need to be stored or shared, and who is responsible for checking data protection rules (unchecked against primary legal text)?

## Next action
Ask the engineering or IT team what sensor data is currently collected from equipment already installed at customer sites. This single fact determines whether a predictive-maintenance pilot is even possible, and should be answered before any supplier conversations or pilot budget is considered.

## Source list with confidence

- Artificial Intelligence / Datatechnologieën - https://fme.nl/nl/artificial-intelligence - Confidence: MEDIUM
- Aan de slag met Artificial Intelligence (AI) - https://smartindustry.nl/aan-de-slag-met-artificial-intelligence-ai - Confidence: MEDIUM
- Onderzoek AI-gebruik in het mkb: Ambitie of aarzeling? - https://open.overheid.nl/documenten/30ab7be6-a0ea-4e4f-bf86-91157c56ccc8/file - Confidence: LOW
- Short-Horizon Predictive Maintenance of Industrial Pumps Using Time-Series Features and Machine Learning - https://arxiv.org/pdf/2508.19974 - Confidence: MEDIUM
- Machine Learning for Pump Predictive Maintenance - https://www.pumpsandsystems.com/machine-learning-pump-predictive-maintenance - Confidence: MEDIUM
