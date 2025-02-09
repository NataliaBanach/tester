from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    #srartujemy przeglądarkę
    browser = p.chromium.launch()
    # otwieramy nowa karte/strone w przeglądarce
    page = browser.new_page()
    # przechodzimy na stronę
    page.goto("https://allegro.pl")
    # pobieramy tyyul strony
    page_title = page.title()
    # drukujemy na konsoli tytuł strony
    print(f"Tytul strony jest {page_title}")

    # sprawdzamy czy tytul strony zawiera oczykiwany tekst
    assert "Onet Jestes na biezaco" in page_title

    # zamykamy przeglądarke
    browser.close()