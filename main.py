# main.py - Main Trading Bot Script

import os
import time
import pandas as pd
import numpy as np
from alpaca import place_order
from alpha_vantage import get_historical_data

# Load API keys from .env
ALPACA_API_KEY = os.getenv("ALPACA_API_KEY")
ALPACA_API_SECRET = os.getenv("ALPACA_API_SECRET")

# Define your trading logic here
def mean_reversion_strategy(symbol):
    """
    Implement a mean-reversion trading strategy for the given symbol.

    Args:
        symbol (str): The trading symbol of the asset.

    Returns:
        None
    """
    # Fetch historical data from Alpha Vantage
    historical_data = get_historical_data(symbol)
    
    # Convert the historical data into a Pandas DataFrame
    df = pd.DataFrame.from_dict(historical_data, orient="index")
    
    # Set the DataFrame index to datetime format
    df.index = pd.to_datetime(df.index)
    
    # Extract the "Close" prices and convert them to float
    df["Close"] = df["4. close"].astype(float)

    # Calculate the mean and standard deviation of historical prices
    mean_price = df["Close"].mean()
    std_price = df["Close"].std()

    # Calculate the Z-score for the current price
    current_price = df["Close"].iloc[-1]
    z_score = (current_price - mean_price) / std_price

    # Define trading rules based on the Z-score
    if z_score > 1.0:
        # Price is significantly above the mean, place a short order
        place_order(symbol, 1, "sell")
    elif z_score < -1.0:
        # Price is significantly below the mean, place a long order
        place_order(symbol, 1, "buy")

# Example usage
if __name__ == "__main__":
    symbol = "AAPL"  # Replace with your desired stock symbol
    
    while True:
        # Execute the mean-reversion strategy for the specified symbol
        mean_reversion_strategy(symbol)
        
        # Pause execution for 60 seconds before the next check
        time.sleep(60)
