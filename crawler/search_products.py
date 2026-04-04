def search_products(keyword, limit=10):
    driver = create_driver()
    url = f"https://search.shopping.naver.com/search/all?query={keyword}"

    products = []

    try:
        driver.get(url)
        time.sleep(3)

        scroll_down(driver)

        items = driver.find_elements(By.CSS_SELECTOR, "div[class^='product_item__']")

        for idx, item in enumerate(items):
            try:
                title = item.find_element(By.CSS_SELECTOR, "a").text
                link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href")

                products.append({
                    "rank": idx + 1,
                    "title": title,
                    "price": "추후 크롤링 가능",
                    "link": link
                })

                if len(products) >= limit:
                    break

            except:
                continue

    finally:
        driver.quit()

    return products
