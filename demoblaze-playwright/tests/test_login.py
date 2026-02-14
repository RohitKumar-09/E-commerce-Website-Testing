from playwright.sync_api import sync_playwright, expect

def test_login_valid_user():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # change to True in CI
        page = browser.new_page()

        page.goto("https://www.demoblaze.com")

        # Click login button
        page.click("#login2")

        # Fill credentials
        page.fill("#loginusername", "admin")
        page.fill("#loginpassword", "admin")

        # Click login inside modal
        page.click("button[onclick='logIn()']")

        # Assertion → username appears in navbar
        expect(page.locator("#nameofuser")).to_contain_text("Welcome")

        browser.close()
