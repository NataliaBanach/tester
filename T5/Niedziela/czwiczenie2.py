from playwright.sync_api import sync_playwright

# Uruchamiamy Playwrighta
with sync_playwright() as p:
    # Uruchamiamy przeglądarkę (może być "chromium", "firefox" lub "webkit")
    browser = p.chromium.launch(headless=False)  # headless=True uruchomi w tle
    page = browser.new_page()

    # Otwieramy stronę logowania
    page.goto("https://practicetestautomation.com/practice-test-login/")  # Podmień na właściwy URL

    # Wypełniamy formularz logowania
    page.fill("#username", "incorrectUser")  # Podmień na rzeczywisty selektor
    page.fill("#password", "Password123")    # Podmień na rzeczywisty selektor
    page.click("#submit")                     # Klikamy przycisk logowania

    # Czekamy na komunikat błędu i sprawdzamy treść
    page.wait_for_selector("#error")  # Podmień na rzeczywisty selektor błędu
    error_text = page.inner_text("#error")

    assert error_text == "Your username is invalid!", f"Niepoprawny tekst błędu: {error_text}"
    print("✅ Test zakończony pomyślnie!")

    # Zamykamy przeglądarkę
    browser.close()
