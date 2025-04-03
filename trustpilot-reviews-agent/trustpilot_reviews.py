import pandas as pd
import asyncio
from pyppeteer import launch

# ### DO NOT CHANGE DATE RANGES
DATE_RANGE_ALL = ""
DATE_RANGE_30DAYS = "date=last30days"
DATE_RANGE_3_MONTHS = "date=last3months"
DATE_RANGE_6_MONTHS = "date=last6months"
DATE_RANGE_12_MONTHS = "date=last12months"
# #########################################

COMPANY_NAME = "[YOUR COMPANY NAME]"    # make sure you check the exact name on TrustPilot website first, else you may not get the relevant results.
REVIEWS_HOMEPAGE = f"https://www.trustpilot.com/review/{COMPANY_NAME}?{DATE_RANGE_12_MONTHS}"

async def init():
    browser = await launch(headless=False)
    page = await browser.newPage()
    reviews = []

    # Load Page 1
    page = await load_page(page, REVIEWS_HOMEPAGE)
    page_navs = await get_navigation(page)
    
    for page_nav in page_navs:
        match page_nav:
            case "Previous":
                pass
            case "Next page":
                pass
            case "1":   # 1st page is already loaded
                reviews = await get_reviews(page)
            case _:
                paged_url = f"{REVIEWS_HOMEPAGE}&page={page_nav}"
                page = await load_page(page, paged_url)
                reviews.extend(await get_reviews(page))


    # Write to CSV
    columns = [
        "review_time",
        "customer_name",
        "review_rating",
        "review_content"
    ]
    df = pd.DataFrame(columns=columns, data=reviews)
    df.to_excel("trustpilot_reviews.xlsx", index=False)

    return

async def load_page(page, url):
    await page.goto(url)

    return page

async def get_navigation(page) -> list:
    await page.waitForSelector('article.paper_paper__EGeEb.paper_square__owXbO.card_card__yyGgu.card_noPadding__OOiac.card_square___AZeg.styles_reviewCard__rvE5E')

    # scrape page navigation
    navLinks = await page.querySelectorAll("nav[role=navigation] a")

    page_nos = []
    for navLink in navLinks:
        navLinkText = await navLink.querySelectorEval("span", "el => el.textContent")
        page_nos.append(navLinkText)

    return page_nos

async def get_reviews(page) -> list:
    records = []
    reviews = await page.querySelectorAll('article.paper_paper__EGeEb.paper_square__owXbO.card_card__yyGgu.card_noPadding__OOiac.card_square___AZeg.styles_reviewCard__rvE5E')

    for review in reviews:
        customer_name = await review.querySelectorEval('a[name=consumer-profile] span', 'el => el.textContent')
        review_content = str(await review.querySelectorEval('div[data-review-content]', 'el => el.textContent'))
        # The review time field contains relative datetime information from the current datetime, which is not usable if review is less than 1 day old
        # So we use the actual timestamp at the end of the comment starting with "Date of exprience: ".
        # review_time = await review.querySelectorEval('time', 'el => el.textContent')
        actual_review_time = review_content.split("Date of experience: ")[1]
        review_rating = await review.querySelectorEval('div[data-service-review-rating]', 'el => el.attributes[1].value')

        records.append({"review_time": actual_review_time.strip(), "customer_name": customer_name.strip(), "review_rating": review_rating, "review_content": review_content.strip()})
    
    return records

asyncio.get_event_loop().run_until_complete(init())