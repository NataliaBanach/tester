from playwright.sync_api import sync_playwright

with open("password.txt") as file:
    password = file.read().strip()  # Usuwa zbędne białe znaki i nową linię


# ✅ Uruchamiamy Playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Przeglądarka w trybie widocznym
    page = browser.new_page()

    # 1️⃣ Otwórz stronę logowania
    page.goto("https://practicetestautomation.com/practice-test-login/")  # Podmień na właściwy URL

    # 2️⃣ Wpisz nazwę użytkownika
    page.fill("#username", "student")  # Podmień na rzeczywisty selektor pola użytkownika

    # 3️⃣ Wpisz hasło pobrane z pliku
    page.fill("#password", password)  # Podmień na rzeczywisty selektor pola hasła

    # 4️⃣ Kliknij przycisk "Submit"
    page.click("#submit")  # Podmień na rzeczywisty selektor przycisku

    # 5️⃣ Zweryfikuj komunikat błędu
    page.wait_for_selector("#error")  # Podmień na rzeczywisty selektor komunikatu błędu
    error_message = page.inner_text("#error")

    # 6️⃣ Sprawdź poprawność komunikatu
    expected_text = "Your password is invalid!"
    assert error_message == expected_text, f"❌ Niepoprawny tekst błędu: {error_message}"

    print("✅ Test zakończony pomyślnie!")

    # Zamykamy przeglądarkę
    browser.close()
