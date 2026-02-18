from pathlib import Path

import pandas as pd

from doctor_scraper.fetch import fetch_html
from doctor_scraper.parse import parse_doctor_cards


DEFAULT_URL = "https://www.medifind.com/specialty/otolaryngology"


def scrape_doctors(url: str = DEFAULT_URL) -> list[dict]:
    html = fetch_html(url)
    return parse_doctor_cards(html)


def run_to_excel(output_path: str, url: str = DEFAULT_URL) -> dict:
    rows = scrape_doctors(url=url)
    df = pd.DataFrame(rows)

    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_excel(out, index=False)

    return {
        "rows": len(df),
        "output_path": str(out),
    }
