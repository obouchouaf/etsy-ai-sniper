import gradio as gr
from scraper import scrape_etsy_top_listings

def search_etsy(keyword):
    listings = scrape_etsy_top_listings(keyword)
    return listings

iface = gr.Interface(fn=search_etsy, inputs="text", outputs="json", title="🛍️ Etsy AI Sniper",
                     description="Enter your product keyword:")
iface.launch()