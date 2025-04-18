import streamlit as st
from scraper import get_etsy_listings
from ai_analysis import analyze_competitors

st.title("🛍️ Etsy AI Sniper")
query = st.text_input("Enter your product keyword:")

if query:
    listings = get_etsy_listings(query)
    st.subheader("Top Listings:")
    st.write(listings)

    if listings:
        with st.spinner("Analyzing with AI..."):
            analysis = analyze_competitors(listings)
        st.subheader("📊 AI Analysis:")
        st.write(analysis)