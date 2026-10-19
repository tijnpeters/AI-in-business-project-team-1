---
title: Geopolitics and Vendor Models
status: APPROVED
---
<!-- published-by: publish_wiki.py -->

# Geopolitics and Vendor Models

!!! warning "Overall confidence: MEDIUM"
    Approved by **Kyran Weijman** on 2026-10-19.
    Research last updated 2026-09-14.
    Next review planned 2026-12-14.


*Who owns this tool — and what happens to you if that changes?*

**Research question:** When an SME like Waterkracht adopts an AI tool, who actually controls it — and what happens to the business if that ownership, access, or the rules around it change?

## Why this matters

Most SMEs buy AI “as a service”: a chatbot, a quoting assistant, a maintenance-prediction tool. Behind the familiar interface usually sits a chain of other companies — the app you actually bought, the AI model it calls behind the scenes, the cloud infrastructure running that model, and the country whose laws govern all three. Waterkracht doesn't need to resolve geopolitics. It needs to know, for every AI tool it adopts, who is really in that chain — and what happens to its data, its quotes and its daily operations if any link changes hands, changes price, or is cut off.

## Three ways this can change under you
**1. Ownership and contracts change upstream — not at your level**

In August 2026, OpenAI told the coding-assistant company Cursor that access to OpenAI's models would end in November 2026, after Cursor's parent company was acquired by SpaceX — not because Cursor's own customers had done anything wrong (CIO, 2026). *The mechanism, not the specific tool, is the lesson: an AI capability can stop working for reasons entirely outside the relationship you have with your own supplier.*

**2. AI infrastructure is concentrated in a small number of providers**

International competition regulators are actively studying how few firms control the chips, cloud capacity and foundation models that most AI tools ultimately run on, and what that concentration means for customers' ability to negotiate or switch (OECD, 2025a; OECD, 2025b). Fewer real alternatives behind the scenes means less leverage for Waterkracht if a vendor changes its terms.

**3. Chips and models are increasingly split along geopolitical lines**

Export controls on advanced AI chips are reshaping who can access which hardware, and analysis of the policy suggests the resulting technology ecosystems will keep diverging rather than converging (Shivakumar, Wessner & Howell / CSIS, 2025). Waterkracht itself is not a target of these controls — but a vendor's own access to the chips or models behind its product can be, and that risk is passed down silently.

## Two questions to ask before you sign anything
**Where does our data actually go?**

If an AI vendor is based outside the EU/EEA, Dutch law requires either a European Commission adequacy decision for that country, or approved contractual safeguards — with extra measures for transfers to the United States since the Schrems II ruling (Autoriteit Persoonsgegevens, n.d.). Ask the vendor in writing which basis applies to your data.

**Could Waterkracht become legally responsible for someone else's AI system?**

Under the EU AI Act, a company that substantially modifies a third-party AI system — or repurposes it beyond its original intended use — can itself become that system's “provider,” inheriting the provider's full compliance obligations, not just a user's (Regulation (EU) 2024/1689, Art. 25). Know, for every AI tool you customise, whether you've crossed that line.

## Checklist — for any AI tool under consideration
- [ ] Who actually runs the model behind this tool — the vendor itself, or a third party?
- [ ] Where is our data stored and processed, and is there a lawful transfer basis?
- [ ] What does the contract say if the vendor's own access to its model or infrastructure is cut off?
- [ ] Is there a working alternative, or an exit plan, if this tool disappears on short notice?
- [ ] Have we changed or repurposed the tool in a way that could make Waterkracht its legal “provider”?

## One thing to do this week
**Before renewing or signing any AI vendor contract, put this question to the vendor in writing: “Which company actually supplies the underlying AI model, where is our data processed, and what is our notice period if that access changes?”** Keep the written answer on file. It is the fastest way to turn this page into a decision.

## How confident are these claims?
HIGH confidence: the Cursor/OpenAI case and the GDPR/EU AI Act rules cited above — primary or directly-reported sources, independently checkable. MEDIUM confidence: the market-concentration and chip-geopolitics claims — grounded in current OECD and CSIS analysis, but these situations are actively moving; re-check figures before citing them in board materials. The CSIS source in particular argues from a US policy-debate perspective and should be read alongside an EU-origin source in a future revision (see Part D, gap analysis).

## Source list with confidence

| Source | AAOCC (weighted /5) | Confidence |
|---|---|---|
| CIO (Ghoshal, A.) (2026, August 31). *Cursor customers will lose access to OpenAI coding models in November.* cio.com | 4.20 | HIGH |
| OECD (2025a). *Competition in artificial intelligence infrastructure.* OECD Publishing | 4.55 | HIGH |
| OECD (2025b). *Competition in the provision of cloud computing services.* OECD Publishing | 4.55 | HIGH |
| Shivakumar, S., Wessner, C., & Howell, T. (2025, April 14). *The Limits of Chip Export Controls in Meeting the China Challenge.* CSIS | 3.65 | MEDIUM |
| Autoriteit Persoonsgegevens (n.d.). *Doorgifte binnen en buiten de EU.* autoriteitpersoonsgegevens.nl | 4.80 | HIGH |
| Regulation (EU) 2024/1689 (AI Act), Art. 25 — accessed via artificialintelligenceact.eu (unchecked against primary legal text on EUR-Lex) | 5.00 | HIGH |
