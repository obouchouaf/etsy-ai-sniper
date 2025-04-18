import requests
from bs4 import BeautifulSoup

def scrape_etsy_top_listings(keyword):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    }
    url = f"https://www.etsy.com/search?q={keyword.replace(' ', '+')}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    listings = []
    for item in soup.select('li.wt-list-unstyled div.v2-listing-card__info a'):
        title = item.get_text(strip=True)
        link = item.get("href")
        if title and link:
            listings.append({"title": title, "url": link})

    return listings[:10]  # Return top 10 listings