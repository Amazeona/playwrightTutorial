import asyncio
from playwright.async_api import async_playwright


async def main():
    with async_playwright() as p:
        browser = await p.firefox.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://practicetestautomation.com/practice-test-login/")
        print(await page.title())

asyncio.run(main())

