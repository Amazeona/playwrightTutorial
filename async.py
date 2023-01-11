import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://practicetestautomation.com/practice-test-login/")
        print(await page.title())
        await browser.close()


asyncio.run(main())

print("testing vs code stage and stuff")
print("right back from pycharm!")
print("testing accessing laptop branch in vsc also")
