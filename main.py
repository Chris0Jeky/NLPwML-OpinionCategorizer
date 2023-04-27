from web_scraping import fetch_data
from text_processing import preprocess_text, extract_adjectives, analyze_sentiment
from visualization import visualize_adjectives

def main():
    # Replace this with the URL you want to scrape
    url = "https://www.example.com"
    text = fetch_data(url)

    processed_tokens = preprocess_text(text)
    adjectives = extract_adjectives(processed_tokens)

    visualize_adjectives(adjectives)

    sentiment_scores = analyze_sentiment(text)
    print(sentiment_scores)

if __name__ == "__main__":
    main()
