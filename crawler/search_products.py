from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from crawler.utils import wait_short


def create_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--window-size=1920,1080")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    )

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def search_products(keyword, limit=10):
    driver = create_driver()
    products = []

    try:
        url = f"https://search.shopping.naver.com/search/all?query={keyword}"
        driver.get(url)
        wait_short(3)

        # 스크롤해서 상품 로딩 유도
        for _ in range(3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            wait_short(2)

        # 네이버 쇼핑 구조는 자주 바뀌므로 여러 선택자 후보 사용
        item_selectors = [
            "div.product_item__MDtDF",
            "div.basicList_item__2XT81",
            "div.adProduct_item__1zC9h"
        ]

        items = []
        for selector in item_selectors:
            items = driver.find_elements(By.CSS_SELECTOR, selector)
            if items:
                break

        for idx, item in enumerate(items[:limit], start=1):
            try:
                title = ""
                link = ""
                price = "가격 없음"

                title_selectors = [
                    "a.product_link__TrAac",
                    "a.basicList_link__JLQJf"
                ]
                for ts in title_selectors:
                    title_elems = item.find_elements(By.CSS_SELECTOR, ts)
                    if title_elems:
                        title = title_elems[0].text.strip()
                        link = title_elems[0].get_attribute("href")
                        break

                price_selectors = [
                    "span.price_num__S2p_v",
                    "span.product_num__fafe5"
                ]
                for ps in price_selectors:
                    price_elems = item.find_elements(By.CSS_SELECTOR, ps)
                    if price_elems:
                        price = price_elems[0].text.strip()
                        break

                if title and link:
                    products.append({
                        "rank": idx,
                        "title": title,
                        "price": price,
                        "link": link
                    })

            except Exception:
                continue

    finally:
        driver.quit()

    return products
