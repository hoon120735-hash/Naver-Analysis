from collections import Counter
from crawler.utils import clean_text


def extract_keywords(reviews, top_n=10):
    words = []

    for review in reviews:
        cleaned = clean_text(review)
        tokens = cleaned.split()

        for token in tokens:
            if len(token) >= 2:
                words.append(token)

    counter = Counter(words)
    return counter.most_common(top_n)
