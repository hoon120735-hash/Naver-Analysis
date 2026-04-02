from crawler.search_products import search_products
from crawler.collect_reviews import collect_reviews
from analysis.keyword_analysis import extract_keywords
from analysis.sentiment_analysis import analyze_sentiment


def main():
    keyword = input("검색할 상품 키워드를 입력하세요: ")

    products = search_products(keyword, limit=10)

    if not products:
        print("검색된 상품이 없습니다.")
        return

    print(f"\n'{keyword}' 검색 결과 상위 {len(products)}개 상품 분석 시작\n")

    for product in products:
        print("=" * 50)
        print(f"순위: {product['rank']}")
        print(f"상품명: {product['title']}")
        print(f"가격: {product['price']}")
        print(f"링크: {product['link']}")

        reviews = collect_reviews(product["link"], limit=20)

        if not reviews:
            print("리뷰를 수집하지 못했습니다.")
            continue

        keywords = extract_keywords(reviews, top_n=5)
        sentiment = analyze_sentiment(reviews)

        print("\n[리뷰 키워드 TOP 5]")
        for word, count in keywords:
            print(f"{word}: {count}")

        print("\n[감성 분석]")
        print(f"총 리뷰 수: {sentiment['total_reviews']}")
        print(f"긍정 리뷰 표현 수: {sentiment['positive']}")
        print(f"부정 리뷰 표현 수: {sentiment['negative']}")

    print("\n분석 완료")


if __name__ == "__main__":
    main()
