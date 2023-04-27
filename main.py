import matplotlib.pyplot as plt
import nltk
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')



text = "Your input text here"
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Tokenization
tokens = word_tokenize(text.lower())

# Remove stopwords and lemmatize
processed_tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalpha() and token not in stop_words]


adjectives = ["fantastic", "great", "amazing", "beautiful", "horrible", "terrible", "awful", "nice"]

wordcloud = WordCloud(background_color='white', width=800, height=800).generate(" ".join(adjectives))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

sia = SentimentIntensityAnalyzer()
text = "The movie was absolutely fantastic but the acting bad."
sentiment_scores = sia.polarity_scores(text)

nlp = spacy.load('en_core_web_sm')
doc = nlp(" ".join(processed_tokens))

adjectives = [token.text for token in doc if token.pos_ == "ADJ"]

print(sentiment_scores)
text = "the acting bad but The movie was absolutely fantastic ."
sentiment_scores = sia.polarity_scores(text)

print(sentiment_scores)

text = "I've got nothing but bad faith "
sentiment_scores = sia.polarity_scores(text)

print(sentiment_scores)
# Output: {'neg': 0.0, 'neu': 0.328, 'pos': 0.672, 'compound': 0.8074}
