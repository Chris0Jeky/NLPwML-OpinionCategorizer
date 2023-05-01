from bs4 import BeautifulSoup
import requests


def fetch_data(url):
    if not url:
        raise ValueError("URL must not be empty")

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()
