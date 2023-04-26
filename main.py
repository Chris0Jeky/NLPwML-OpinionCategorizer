from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
text = "The movie was absolutely fantastic but the acting bad."
sentiment_scores = sia.polarity_scores(text)

print(sentiment_scores)
# Output: {'neg': 0.0, 'neu': 0.328, 'pos': 0.672, 'compound': 0.8074}
