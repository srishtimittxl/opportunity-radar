import requests
import pandas as pd

def fetch_bulk_deals():
    print("Fetching bulk deals data...")

    # Using a more accessible data source
    url = "https://archives.nseindia.com/archives/equities/bultdeal/MW-BULKDEALS.csv"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    }

    response = requests.get(url, headers=headers)
    
    # Check if we got a valid response
    print(f"Response status: {response.status_code}")
    
    if response.status_code == 200:
        from io import StringIO
        df = pd.read_csv(StringIO(response.text))
        print("\n✅ Today's Bulk Deals:")
        print(df.head(10).to_string(index=False))
        return df
    else:
        print("❌ NSE blocked us. Using sample data instead...")
        return use_sample_data()

def use_sample_data():
    # Realistic sample data to build and test with
    sample = {
        'Symbol':     ['ZOMATO', 'INFY',   'IRCTC',  'TATAMOTORS', 'HDFCBANK'],
        'Client':     ['XYZ Fund', 'ABC LLC', 'DEF Fund', 'GHI Capital', 'JKL Trust'],
        'Deal Type':  ['BUY', 'SELL', 'BUY', 'BUY', 'SELL'],
        'Quantity':   [4500000, 1200000, 800000, 2300000, 950000],
        'Price (₹)':  [198.3, 1423.1, 712.5, 891.2, 1654.8]
    }
    df = pd.DataFrame(sample)
    print("\n✅ Sample Bulk Deals Data:")
    print(df.to_string(index=False))
    return df

# Run it
fetch_bulk_deals()

# Run It Again python fetch_data.py