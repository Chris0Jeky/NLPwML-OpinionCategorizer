import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import spacy

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

nlp = spacy.load('en_core_web_sm')
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()


def preprocess_text(text):
    if not text:
        raise ValueError("Text must not be empty")

    tokens = word_tokenize(text.lower())
    processed_tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalpha() and token not in stop_words]
    return processed_tokens


def extract_adjectives(processed_tokens):
    if not processed_tokens:
        raise ValueError("Processed tokens must not be empty")

    doc = nlp(" ".join(processed_tokens))
    adjectives = [token.text for token in doc if token.pos_ == "ADJ"]
    return adjectives


def analyze_sentiment(text):
    from nltk.sentiment import SentimentIntensityAnalyzer
    if not text:
        raise ValueError("Text must not be empty")

    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)
    return sentiment_scores
