# PRISM 2.0 — Product Decision Lab

An interactive, polished, offline-capable product strategy demonstration inspired by the Software Product Manager / Life Science NPI vacancy shared by the user. Built to demonstrate **what to develop and why**, not project scheduling or technical delivery management.

## Run
Open `index.html` in a modern browser. For a development workflow, open the folder in VS Code and use Live Server. No npm, API keys, accounts or build process. The Google Fonts import is optional: system fonts are used if offline.

## Working features
- Seven connected sections: Overview, Customer signals, Decision engine, Requirements studio, Platform architecture, Product lifecycle, Executive brief.
- Four editable strategic weights and four context presets recalculate opportunity ranking and recommendations across the workspace.
- Add/remove customer discovery notes, with evidence maturity labels.
- Edit and save outcome-based requirements for each opportunity; live need-to-validation traceability preview.
- Toggle shared capabilities and see the platform strategy reflected in the executive brief.
- Select five product lifecycle/NPI phases, check illustrative decision gates, and update the brief.
- Download a plain-text decision memo, copy it (when browser permissions allow), or print/save as PDF.
- Local storage persists changes; Reset restores defaults.
- Responsive layouts for desktop and mobile.

## Demo flow (3–4 minutes)
1. Overview: explain the fictional portfolio and proposed north-star metric.
2. Customer signals: show that hypotheses are not evidence, and add a discovery observation.
3. Decision engine: switch from Balanced to Quality & trust; show the recommendation update. Change weights and explain the trade-off.
4. Requirements studio: edit a customer need, measurable outcome and validation plan.
5. Platform architecture: evaluate common audit, identity and interoperability capabilities versus instrument-specific logic.
6. Product lifecycle: choose Validate and discuss go / revise / stop decision criteria.
7. Executive brief: export the rationale and required evidence.

## Scientific and professional integrity
All product names, user statements, numbers, ratings, opportunities and decision outputs are fictional and illustrative. This is not a validated clinical, regulatory, quality, financial, or market assessment. The application is not affiliated with Prevas or its undisclosed client. Applicability of standards and regulatory requirements depends on actual intended use, product classification, markets and quality system.

## Files
- `index.html` — interface and semantic content
- `styles.css` — responsive visual design
- `app.js` — interactive logic and local persistence
- `README.md` — this guide
