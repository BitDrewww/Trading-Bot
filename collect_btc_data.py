import pandas as pd
import requests

# Alpha Vantage API Key
api_key = "NJM59VPWJBKWNCIG"

# Define the symbol and endpoint
symbol = "BTC"
endpoint = "https://www.alphavantage.co/query"

# API request parameters
params = {
    "function": "DIGITAL_CURRENCY_DAILY",  # Use the correct function for daily data
    "symbol": symbol,
    "market": "USD",  # Use the market parameter for the currency
    "apikey": api_key,
}

# Send the API request
response = requests.get(endpoint, params=params)
data = response.json()

# Check if the response contains an 'Time Series (Digital Currency Daily)' key
if 'Time Series (Digital Currency Daily)' in data:
    time_series_data = data['Time Series (Digital Currency Daily)']
    
    # Convert the data to a DataFrame
    df = pd.DataFrame.from_dict(time_series_data, orient='index')
    df.index = pd.to_datetime(df.index)
    
    # Save the data to a CSV file
    df.to_csv("BTC_data.csv")
else:
    print("Response does not contain the expected data structure.")

