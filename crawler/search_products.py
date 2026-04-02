import requests
from bs4 import BeautifulSoup


def search_products(keyword, limit=10):
    url = f"https://search.shopping.naver.com/search/all?query={keyword}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    products = []
    items = soup.select("div.basicList_info_area__17Xyo")

    for idx, item in enumerate(items[:limit], start=1):
        title_tag = item.select_one("a.basicList_link__JLQJf")
        price_tag = item.select_one("span.price_num__S2p_v")

        title = title_tag.get_text(strip=True) if title_tag else "상품명 없음"
        link = title_tag["href"] if title_tag and title_tag.has_attr("href") else ""
        price = price_tag.get_text(strip=True) if price_tag else "가격 없음"

        products.append({
            "rank": idx,
            "title": title,
            "price": price,
            "link": link
        })

    return products
