import requests


def fetch_html(url: str, timeout: int = 25) -> str:
    r = requests.get(url, timeout=timeout)
    r.raise_for_status()
    return r.text
