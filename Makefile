.PHONY: install run-api scrape test lint

install:
	python -m venv .venv && . .venv/bin/activate && pip install -e .[dev]

run-api:
	uvicorn doctor_scraper.api.main:app --reload --port 8600

scrape:
	python scripts/run_scraper.py --output data/doctors.xlsx

test:
	pytest

lint:
	ruff check src tests scripts
