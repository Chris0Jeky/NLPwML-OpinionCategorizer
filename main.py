from nltk.sentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

adjectives = ["fantastic", "great", "amazing", "beautiful", "horrible", "terrible", "awful", "nice"]

wordcloud = WordCloud(background_color='white', width=800, height=800).generate(" ".join(adjectives))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

sia = SentimentIntensityAnalyzer()
text = "The movie was absolutely fantastic but the acting bad."
sentiment_scores = sia.polarity_scores(text)

print(sentiment_scores)
text = "the acting bad but The movie was absolutely fantastic ."
sentiment_scores = sia.polarity_scores(text)

print(sentiment_scores)

text = "I've got nothing but bad faith "
sentiment_scores = sia.polarity_scores(text)

print(sentiment_scores)
# Output: {'neg': 0.0, 'neu': 0.328, 'pos': 0.672, 'compound': 0.8074}
