from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from crawler.search_products import create_driver
from crawler.utils import wait_short


def collect_reviews(product_link, limit=30):
    driver = create_driver()
    reviews = []

    try:
        driver.get(product_link)
        wait_short(3)

        # 리뷰 탭 클릭 시도
        review_tab_selectors = [
            "//a[contains(., '리뷰')]",
            "//button[contains(., '리뷰')]",
            "//li[contains(., '리뷰')]"
        ]

        clicked = False
        for selector in review_tab_selectors:
            try:
                review_tab = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, selector))
                )
                driver.execute_script("arguments[0].click();", review_tab)
                wait_short(2)
                clicked = True
                break
            except Exception:
                continue

        # 리뷰 더 보기 / 스크롤
        for _ in range(5):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            wait_short(2)

            more_button_selectors = [
                "//a[contains(., '더보기')]",
                "//button[contains(., '더보기')]"
            ]

            for selector in more_button_selectors:
                try:
                    buttons = driver.find_elements(By.XPATH, selector)
                    for btn in buttons:
                        if btn.is_displayed() and btn.is_enabled():
                            driver.execute_script("arguments[0].click();", btn)
                            wait_short(1)
                except Exception:
                    continue

        review_selectors = [
            "div.reviewItems_text__XIsTc",
            "div._2L3vDiadT9",
            "span._2L3vDiadT9",
            "p.review_text__2QRKs",
            "div.review_text"
        ]

        collected = []
        for selector in review_selectors:
            elems = driver.find_elements(By.CSS_SELECTOR, selector)
            if elems:
                collected = elems
                break

        for elem in collected:
            text = elem.text.strip()
            if text and text not in reviews:
                reviews.append(text)
            if len(reviews) >= limit:
                break

    except Exception as e:
        print(f"리뷰 수집 실패: {e}")

    finally:
        driver.quit()

    return reviews
