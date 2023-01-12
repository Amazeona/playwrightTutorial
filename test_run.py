from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(my_playwright: Playwright) -> None:
    # Go to website
    browser = my_playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")

    # Login
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("student")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("Password123")
    page.get_by_role("button", name="Submit").click()

    # Asserts
    assert page.get_by_role("heading", name="Logged In Successfully")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_run(playwright)
