from crawler.search_products import search_products
from crawler.collect_reviews import collect_reviews
from analysis.keyword_analysis import extract_keywords
from analysis.sentiment_analysis import analyze_sentiment


def main():
    keyword = input("검색할 키워드를 입력하세요: ").strip()

    if not keyword:
        print("키워드를 입력해주세요.")
        return

    print(f"\n'{keyword}' 검색 중...")
    products = search_products(keyword, limit=10)

    if not products:
        print("상품을 찾지 못했습니다.")
        return

    print(f"\n검색 결과 순서대로 상위 {len(products)}개 상품 분석 시작\n")

    for product in products:
        print("=" * 60)
        print(f"순위: {product['rank']}")
        print(f"상품명: {product['title']}")
        print(f"가격: {product['price']}")
        print(f"링크: {product['link']}")

        reviews = collect_reviews(product["link"], limit=30)

        if not reviews:
            print("리뷰를 수집하지 못했습니다.")
            continue

        print(f"수집 리뷰 수: {len(reviews)}")

        keywords = extract_keywords(reviews, top_n=5)
        sentiment = analyze_sentiment(reviews)

        print("\n[키워드 TOP 5]")
        for word, count in keywords:
            print(f"- {word}: {count}")

        print("\n[감성 분석]")
        print(f"- 총 리뷰 수: {sentiment['total_reviews']}")
        print(f"- 긍정 표현 수: {sentiment['positive']}")
        print(f"- 부정 표현 수: {sentiment['negative']}")
        print(f"- 전체 판단: {sentiment['overall']}")

    print("\n모든 분석이 완료되었습니다.")


if __name__ == "__main__":
    main()
