import matplotlib.pyplot as plt
from wordcloud import WordCloud


def visualize_adjectives(adjectives):
    if not adjectives:
        raise ValueError("Adjectives list must not be empty")

    wordcloud = WordCloud(background_color='white', width=800, height=800).generate(" ".join(adjectives))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
