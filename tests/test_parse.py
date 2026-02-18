from doctor_scraper.parse import parse_doctor_cards


def test_parse_doctor_cards() -> None:
    html = '''
    <div class="Card_card__BOrl4">
      <div class="DoctorCard_header__name--text__KqOEk">Dr. Jane Doe</div>
      <div class="CardAddress_card-address__content__+MaVd">
        <div>New York</div><div>USA</div>
      </div>
    </div>
    '''

    out = parse_doctor_cards(html)
    assert len(out) == 1
    assert out[0]["doctor_name"] == "Dr. Jane Doe"
    assert "New York" in out[0]["address"]
