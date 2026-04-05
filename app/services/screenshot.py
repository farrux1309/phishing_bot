import asyncio
from playwright.async_api import async_playwright

async def take_screenshot(url: str) -> bytes | None:
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                viewport={"width": 1280, "height": 720},
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
            )
            page = await context.new_page()

            # Rasm va fontlarni yuklamaslik — tezroq
            await page.route("**/*.{png,jpg,jpeg,gif,svg,woff,woff2,ttf}", 
                           lambda route: route.abort())

            await page.goto(url, timeout=8000, wait_until="domcontentloaded")
            await page.wait_for_timeout(1500)
            screenshot = await page.screenshot(type="png", full_page=False)
            await browser.close()
            return screenshot
    except:
        return None

def get_screenshot(url: str) -> bytes | None:
    return asyncio.run(take_screenshot(url))