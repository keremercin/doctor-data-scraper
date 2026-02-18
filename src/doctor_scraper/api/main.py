from fastapi import FastAPI

from doctor_scraper.pipeline import DEFAULT_URL, scrape_doctors

app = FastAPI(title="Doctor Data Scraper API", version="0.2.0")


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "doctor-scraper"}


@app.get("/v1/doctors")
def doctors(url: str = DEFAULT_URL) -> dict:
    rows = scrape_doctors(url=url)
    return {"count": len(rows), "items": rows}
