from playwright.sync_api import sync_playwright

# Uruchamiamy Playwrighta
with sync_playwright() as p:
    # Uruchamiamy przeglądarkę (chromium, firefox lub webkit)
    browser = p.chromium.launch(headless=False)  # headless=False -> widoczna przeglądarka
    page = browser.new_page()

    # 1️⃣ Otwórz stronę logowania
    page.goto("https://practicetestautomation.com/practice-test-login/")  # Podmień na rzeczywisty URL

    # 2️⃣ Wpisz poprawną nazwę użytkownika
    page.fill("#username", "student")  # Podmień na rzeczywisty selektor pola użytkownika

    # 3️⃣ Wpisz niepoprawne hasło
    page.fill("#password", "incorrectPassword")  # Podmień na rzeczywisty selektor pola hasła

    # 4️⃣ Kliknij przycisk "Submit"
    page.click("#submit")  # Podmień na rzeczywisty selektor przycisku

    # 5️⃣ Zweryfikuj, czy komunikat błędu jest wyświetlony
    page.wait_for_selector("#error")  # Podmień na rzeczywisty selektor komunikatu błędu
    error_message = page.inner_text("#error")

    # 6️⃣ Sprawdź, czy komunikat ma poprawny tekst
    expected_text = "Your password is invalid!"
    assert error_message == expected_text, f"❌ Niepoprawny tekst błędu: {error_message}"

    print("✅ Test zakończony pomyślnie!")

    # Zamykamy przeglądarkę
    browser.close()
