positive_words = ["좋아요", "만족", "추천", "훌륭", "최고", "빠름", "예쁨", "편리", "튼튼", "재구매"]
negative_words = ["별로", "불만", "느림", "나쁨", "최악", "불편", "아쉬움", "실망", "비쌈", "문제"]


def analyze_sentiment(reviews):
    positive_count = 0
    negative_count = 0

    for review in reviews:
        for word in positive_words:
            if word in review:
                positive_count += 1

        for word in negative_words:
            if word in review:
                negative_count += 1

    total = len(reviews)

    return {
        "total_reviews": total,
        "positive": positive_count,
        "negative": negative_count
    }
