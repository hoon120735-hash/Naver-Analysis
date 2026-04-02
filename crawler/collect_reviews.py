import requests
from bs4 import BeautifulSoup


def collect_reviews(product_link, limit=20):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    reviews = []

    try:
        response = requests.get(product_link, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        review_tags = soup.select("div.reviewItems_text__XIsTc, div._2L3vDiadT9, span._2L3vDiadT9")

        for tag in review_tags[:limit]:
            text = tag.get_text(strip=True)
            if text:
                reviews.append(text)

    except Exception as e:
        print(f"리뷰 수집 실패: {e}")

    return reviews
