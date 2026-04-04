from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from crawler.search_products import search_products
from crawler.collect_reviews import collect_reviews
from analysis.sentiment_analysis import analyze_sentiment
from analysis.keyword_analysis import extract_keywords

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health_check():
    return {"message": "Naver Analysis API is running"}


@app.get("/search")
def search(keyword: str = Query(...), limit: int = 5):
    results = search_products(keyword, limit)
    return {
        "keyword": keyword,
        "results": results
    }


@app.get("/analyze")
def analyze(product_url: str, review_limit: int = 10):
    reviews = collect_reviews(product_url, review_limit)
    sentiment = analyze_sentiment(reviews)
    keywords = extract_keywords(reviews)

    return {
        "product_url": product_url,
        "reviews": reviews,
        "sentiment": sentiment,
        "keywords": keywords
    }
