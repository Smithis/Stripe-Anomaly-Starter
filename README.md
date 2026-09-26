# Payments Anomaly Starter (Stripe-intern style) - Charan Teja
Mirrors recent Stripe intern themes: generalized anomaly detection, safer payouts, fraud controls.

## Why this closes JD gaps
- Production habits: PR-ready code + pytest + coverage, multi-person feedback loop (CONTRIBUTING.md).
- Multi-language navigation: Python core + Go client stub in `client-go/` (learn Go basics, JD stack Ruby/Java/JS/Go/Scala).
- AI tools with judgment: used for scaffolding, all outputs reviewed + tested (JD requirement).

## Run
```bash
pip install -r requirements.txt
pytest -q
python anomaly.py
uvicorn app:app --reload
```

## Learn next (for Stripe bar)
- Go basics: run `go run ./client-go`, add retry/timeout
- Tests to 90% coverage, add GitHub Actions CI
- Write 1-page design doc in `docs/DESIGN.md` (problem, tradeoffs, fraud precision/recall)
