#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import json
import requests
from datetime import datetime

# Securely load API key from GitHub Secrets or local environment
API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

# Stock ticker
SYMBOL = "NVDA"

# Alpha Vantage endpoint
url = (
    f"https://www.alphavantage.co/query"
    f"?function=GLOBAL_QUOTE"
    f"&symbol={SYMBOL}"
    f"&apikey={API_KEY}"
)

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    # Extract stock information
    quote = data.get("Global Quote", {})

    output = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "symbol": SYMBOL,
        "price": quote.get("05. price"),
        "volume": quote.get("06. volume"),
        "change_percent": quote.get("10. change percent")
    }

    # Create data folder if it does not exist
    os.makedirs("data", exist_ok=True)

    # Save JSON output
    with open("data/stock_data.json", "w") as f:
        json.dump(output, f, indent=4)

    print("Stock data updated successfully.")
    print(json.dumps(output, indent=4))

except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")

except Exception as e:
    print(f"Unexpected error: {e}")


# In[4]:


#!pip install requests

