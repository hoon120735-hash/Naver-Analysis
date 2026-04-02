from collections import Counter
from crawler.utils import clean_text


STOPWORDS = {
    "정말", "진짜", "그냥", "너무", "아주", "조금", "사용", "구매",
    "상품", "제품", "생각", "느낌", "하나", "이번", "처음", "배송"
}


def extract_keywords(reviews, top_n=10):
    words = []

    for review in reviews:
        cleaned = clean_text(review)
        tokens = cleaned.split()

        for token in tokens:
            if len(token) >= 2 and token not in STOPWORDS:
                words.append(token)

    counter = Counter(words)
    return counter.most_common(top_n)
