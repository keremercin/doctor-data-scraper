from bs4 import BeautifulSoup


def parse_doctor_cards(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    rows = []

    cards = soup.select(".Card_card__BOrl4")
    for c in cards:
        name = c.select_one(".DoctorCard_header__name--text__KqOEk")
        address_container = c.find(class_=lambda cls: isinstance(cls, str) and "CardAddress_card-address__content__" in cls)
        address_parts = address_container.find_all("div") if address_container else []

        doctor_name = name.get_text(strip=True) if name else "Information Not Available"
        address = " ".join([x.get_text(strip=True) for x in address_parts]) if address_parts else "Information Not Available"

        rows.append(
            {
                "doctor_name": doctor_name,
                "address": address,
            }
        )

    return rows
