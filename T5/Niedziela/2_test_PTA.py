from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # przechodzimy na stronę logowania
    page.goto("https://practicetestautomation.com/practice-test-login/")
    # wprowadzenie username
    page.fill("#username", "student")
    # wprowadzenie password
    page.fill("#password", "Password123")
    # klikniecie przycisku logowania
    page.click("#submit")
    # sprawdzenie czy przekierowalo nas na strone z sukcesem
    page.wait_for_url("**/logged-in-successfully/")

    #page_url = page.url
    assert page.url in "https://practicetestautomation.com/logged-in-successfully/"

    #logged in successfully
    success_text = "Logged In Successfully"
    text = page.text_content("h1")
    print(f"Zawartosc naglowka to: {text}")

    assert success_text in text

    # sprawdzenie czy przycisk log out jest widoczny
    locator_logout = page.locator("text=Log out").is_visible()
    assert locator_logout is True

    browser.close()
  
   