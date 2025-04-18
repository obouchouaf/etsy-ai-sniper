import openai
import os

# Load API key from environment variable (recommended)
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_competitors(listings):
    prompt = f"Analyze these Etsy listings and provide insights:\n{listings}"
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a data analyst specialized in e-commerce trends."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content