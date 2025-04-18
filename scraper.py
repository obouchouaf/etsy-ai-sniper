import requests
from bs4 import BeautifulSoup

def get_etsy_listings(query):
    url = f"https://www.etsy.com/search?q={query.replace(' ', '+')}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('li', {'class': 'wt-list-unstyled'})[:5]
    listings = [item.get_text(strip=True) for item in items if item]
    return listings