from doctor_scraper import pipeline


def test_pipeline(monkeypatch) -> None:
    fake_html = '<div class="Card_card__BOrl4"><div class="DoctorCard_header__name--text__KqOEk">Dr. X</div></div>'
    monkeypatch.setattr(pipeline, "fetch_html", lambda url: fake_html)

    out = pipeline.scrape_doctors(url="https://example.com")
    assert len(out) == 1
    assert out[0]["doctor_name"] == "Dr. X"
