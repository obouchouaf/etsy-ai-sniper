
import streamlit as st
from scraper import scrape_etsy
from ai_analysis import analyze_competitors

st.title("Etsy Competitor Sniper 🔍")
keyword = st.text_input("Enter a product keyword:")

if keyword:
    with st.spinner("Scraping Etsy..."):
        listings = scrape_etsy(keyword)
    st.write("### Top Listings:", listings)
    with st.spinner("Analyzing with AI..."):
        analysis = analyze_competitors(listings)
    st.write("### AI Insights:")
    st.text(analysis)
