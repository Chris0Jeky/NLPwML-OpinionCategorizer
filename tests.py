import unittest
from web_scraping import fetch_data
from text_processing import preprocess_text, extract_adjectives, analyze_sentiment
from visualization import visualize_adjectives


class TestFunctions(unittest.TestCase):
    def test_fetch_data(self):
        url = "https://github.com/Chris0Jeky"
        text = fetch_data(url)
        self.assertIsInstance(text, str)

    def test_preprocess_text(self):
        text = "This is a sample text."
        processed_tokens = preprocess_text(text)
        self.assertIsInstance(processed_tokens, list)

    def test_extract_adjectives(self):
        tokens = ["beautiful", "car", "fast", "red"]
        adjectives = extract_adjectives(tokens)
        self.assertEqual(adjectives, ["beautiful", "red"])

    def test_analyze_sentiment(self):
        text = "This is a fantastic day."
        sentiment_scores = analyze_sentiment(text)
        self.assertIsInstance(sentiment_scores, dict)

    def test_visualize_adjectives(self):
        adjectives = ["fantastic", "great", "amazing", "beautiful", "horrible", "terrible", "awful", "nice"]
        try:
            visualize_adjectives(adjectives)
        except Exception as e:
            self.fail("visualize_adjectives() raised an exception: " + str(e))

    if __name__ == '__main__':
        unittest.main()
