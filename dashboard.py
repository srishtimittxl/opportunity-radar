import streamlit as st
import pandas as pd
from groq import Groq
import os
from dotenv import load_dotenv
from fetch_data import fetch_bulk_deals

load_dotenv()

st.set_page_config(page_title="Opportunity Radar", page_icon="📡")
st.title("📡 Opportunity Radar")
st.subheader("AI-powered stock signals for Indian retail investors")

# Fetch data
df = fetch_bulk_deals()

st.markdown("### 📊 Today's Bulk Deals")
st.dataframe(df, width='stretch')

# AI Analysis button
if st.button("🤖 Generate AI Signal"):
    with st.spinner("Analyzing market data..."):
        data_text = df.to_string(index=False)
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{
                "role": "user",
                "content": f"""You are a smart stock market analyst for Indian retail investors.

Here are today's bulk deals on NSE:

{data_text}

Please:
1. Identify the most interesting signal (BUY or SELL)
2. Explain in 2-3 simple sentences why a retail investor should pay attention
3. Give a simple verdict: Bullish / Bearish / Watch

Keep it simple — the reader is a beginner investor."""
            }]
        )
        analysis = response.choices[0].message.content
        st.markdown("### 🤖 AI Signal")
        st.success(analysis)

st.markdown("---")
st.caption("Data sourced from NSE | Powered by Groq AI")
