from groq import Groq
import os
from dotenv import load_dotenv
from fetch_data import fetch_bulk_deals

# Load API keys
load_dotenv()

# Fetch stock data
df = fetch_bulk_deals()
data_text = df.to_string(index=False)

# Connect to Groq (free!)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

print("\n⏳ Sending data to AI for analysis...")

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",

    messages=[
        {
            "role": "user",
            "content": f"""You are a smart stock market analyst for Indian retail investors.

Here are today's bulk deals on NSE:

{data_text}

Please:
1. Identify the most interesting signal (BUY or SELL)
2. Explain in 2-3 simple sentences why a retail investor should pay attention
3. Give a simple verdict: Bullish / Bearish / Watch

Keep it simple — the reader is a beginner investor."""
        }
    ]
)

analysis = response.choices[0].message.content
print("\n🤖 AI Analysis:")
print(analysis)
