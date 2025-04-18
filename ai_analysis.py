
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_competitors(listings):
    input_text = "".join([f"Title: {x['title']}, Price: {x['price']}\n" for x in listings])
    prompt = f"""
    Here is a list of Etsy listings:
    {input_text}
    
    Please identify:
    1. What makes the top ones successful
    2. Pricing trends
    3. Suggest a better listing title and strategy
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
