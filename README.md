# opportunity-radar

AI-powered stock signal detector for Indian retail investors.

## What it does
Monitors NSE bulk deals and uses AI to surface the most 
significant signals — explained in plain English.

## How to run
1. Clone this repo
2. Install dependencies: `pip install groq streamlit pandas requests python-dotenv`
3. Add your Groq API key to a `.env` file: `GROQ_API_KEY=your-key`
4. Run: `streamlit run dashboard.py`

## Tech Stack
- Python + Streamlit (dashboard)
- Groq AI / LLaMA 3.1 (signal analysis)
- NSE data (bulk deals)

## Built for
ET Markets Hackathon 2026
```

Then commit it:
```
git add README.md
git commit -m "Add README"
git push