# 🩺 doctor-data-scraper

[![CI](https://github.com/keremercin/doctor-data-scraper/actions/workflows/ci.yml/badge.svg)](https://github.com/keremercin/doctor-data-scraper/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688)

Doctor profile extraction pipeline with API and batch export.

## What it does
- extracts doctor name + address from directory cards
- exposes API endpoint for quick integration
- supports Excel export for operational use

> Use responsibly and follow source terms and privacy rules.

---

## API
- `GET /health`
- `GET /v1/doctors`

Swagger: `http://localhost:8600/docs`

---

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]

# Run API
uvicorn doctor_scraper.api.main:app --reload --port 8600

# Export to Excel
python scripts/run_scraper.py --output data/doctors.xlsx
```

---

## Structure

```text
src/doctor_scraper/
├─ api/main.py
├─ fetch.py
├─ parse.py
└─ pipeline.py
```

---

## Quality
- tests + CI
- modular pipeline design
- lint checks

---

## Docs
- `docs/CASE_STUDY.md`
