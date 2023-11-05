# alpaca.py - Alpaca API Interaction

import os
import alpaca_trade_api as tradeapi

# Load API keys from .env
ALPACA_API_KEY = os.getenv("ALPACA_API_KEY")
ALPACA_API_SECRET = os.getenv("ALPACA_API_SECRET")

# Create an Alpaca API client using the provided API keys
api = tradeapi.REST(ALPACA_API_KEY, ALPACA_API_SECRET, base_url="https://paper-api.alpaca.markets")
# We use the paper trading API (https://paper-api.alpaca.markets) for testing purposes.

def place_order(symbol, qty, side):
    """
    Place a trading order using Alpaca API.

    Args:
        symbol (str): The trading symbol of the asset.
        qty (int): The quantity of the asset to trade.
        side (str): The side of the order, either "buy" or "sell".

    Returns:
        None
    """
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side=side,
        type="limit",          # We use a limit order type.
        time_in_force="gtc",   # Good 'til canceled time in force.
        limit_price=100,       # Set your desired limit price here.
    )
