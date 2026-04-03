import requests
from bs4 import BeautifulSoup
from urllib.parse import quote


def search_products(keyword, limit=10):
    query = quote(keyword)
    url = f"https://search.shopping.naver.com/search/all?query={query}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    products = []
    links = soup.select("a")

    for idx, link in enumerate(links, start=1):
        title = link.get_text(strip=True)
        href = link.get("href")

        if title and href and len(title) > 1:
            products.append({
                "rank": len(products) + 1,
                "title": title,
                "price": "가격 정보 없음",
                "link": href
            })

        if len(products) >= limit:
            break

    return products
