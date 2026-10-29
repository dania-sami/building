# ATLAS Impact Studio | An independent Ericsson role-inspired portfolio concept

A proposed first product increment for a leader-facing workforce AI assistant. **Not affiliated with Ericsson. No Ericsson data or systems used.** All workforce data are synthetic.

## Why this increment
- Give leaders useful aggregate workforce answers grounded in approved metrics.
- Explicitly abstain when data are missing or requests are inappropriate.
- Capture leader feedback to drive weekly iteration.
- Show real code, SQL-backed calculations, API response contracts and executable tests.

## Run the interactive product experience
Open `index.html` directly. This includes a fully offline simulation and an additional "Impact studio" area. For live SQL-backed answers, start the backend:

```bash
python -m venv .venv
source .venv/bin/activate # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn backend.app:app --reload --port 8000
```

Then use the "Live API" controls in the Impact Studio panel. Open `http://localhost:8000/docs` to inspect the API.

## Test
```bash
pytest -q
```

## Design principles
1. **Answer contracts:** Grounded / refused / abstained / clarification.
2. **Evidence:** Explicit source table, field and operation, not unverifiable citations.
3. **Honesty:** A single snapshot cannot support a trend. Mobility events are not automatically a rate.
4. **Privacy:** No employee-level data exist in the demo. Production requires authentication, authorisation, row-level controls, logging policies, security review and privacy assessment.
5. **Adoption:** Real leader usage is unknown. Targets are hypotheses, not results.

## Proposed first weeks, not completed Ericsson work
- Week 1: Interview leaders, choose top recurring aggregate questions, define answer contracts.
- Week 2: Build trusted retrieval and evaluation checks with a product engineer and technical lead.
- Week 3: Pilot with authorised users, inspect failed questions and confusion.
- Week 4: Improve quality and latency; ship or remove features based on measured usage.

## Production gaps
This demo is a Python/FastAPI/SQLite reference implementation, **not** a Snowflake integration, an LLM deployment, an authenticated HR system or a production-ready service. The offline HTML uses deterministic canned logic; the API is separate and uses SQL-backed results. Do not use with real people data without full security, privacy and governance work.
