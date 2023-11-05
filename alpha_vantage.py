# alpha_vantage.py - Alpha Vantage API Interaction

import os
import requests

# Load API key from .env
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

def get_historical_data(symbol, interval="1min"):
    """
    Fetch historical price data for a given asset symbol from Alpha Vantage API.

    Args:
        symbol (str): The trading symbol of the asset.
        interval (str, optional): The time interval for historical data (default is "1min").

    Returns:
        dict: A dictionary containing historical price data.
    """
    # Construct the API URL with the provided symbol, interval, and API key
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={ALPHA_VANTAGE_API_KEY}"
    
    # Send a GET request to the Alpha Vantage API
    response = requests.get(url)
    
    # Parse the JSON response into a Python dictionary
    data = response.json()
    
    # Return the time series data corresponding to the specified interval
    return data["Time Series ({})".format(interval)]
