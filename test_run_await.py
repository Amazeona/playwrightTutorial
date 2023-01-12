import asyncio

from playwright.async_api import Playwright, async_playwright, expect


async def test_run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://practicetestautomation.com/practice-test-login/")
    await page.get_by_label("Username").click()
    await page.get_by_label("Username").fill("student")
    await page.get_by_label("Password").click()
    await page.get_by_label("Password").fill("Password123")
    await page.get_by_role("button", name="Submit").click()

    assert page.get_by_role("heading", name="Logged In Successfully").click()

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await test_run(playwright)


asyncio.run(main())
