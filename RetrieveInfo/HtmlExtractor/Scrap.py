import asyncio
from playwright.async_api import async_playwright

tabs = ["fees", "reviews"]
tabs = ['']

async def scroll_page(page) -> None:
    """
    Scrolls a webpage to load all its content.

    Args:
        page: The webpage to scroll, represented as a Pyppeteer Page object.

    Returns:
        None

    Example usage:
        page = await browser.newPage()
        await page.goto("https://www.example.com")
        await scroll_page(page)
    """
    # Get the initial height of the page
    previous_height = await page.evaluate('() => document.body.scrollHeight')
    
    while True:
        await page.evaluate('() => window.scrollTo(0, document.body.scrollHeight)')
        await asyncio.sleep(6)
        new_height = await page.evaluate('() => document.body.scrollHeight')
        if new_height == previous_height:
            break
        
        previous_height = new_height

async def main(tab: str) -> None:
    """
    Scrapes a webpage and saves its content to an HTML file.

    Args:
        tab (str): The URL parameter to append to the base URL.

    Returns:
        None

    Example usage:
        await main("path/to/tab")
    """
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto('https://www.shiksha.com/college/government-arts-college-dausa-110155' + tab)
        await scroll_page(page)
        
        content = await page.content()

        with open(f'scraped_page{tab}.html', 'w', encoding='utf-8') as f:
            f.write(content)
        
        await browser.close()

for i in tabs:
    asyncio.run(main(i))