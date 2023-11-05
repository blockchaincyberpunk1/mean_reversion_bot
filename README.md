# Mean Reversion Trading Bot

  [![License](https://img.shields.io/static/v1?label=License&message=MIT&color=blue&?style=plastic&logo=appveyor)](https://opensource.org/license/MIT)



## Table Of Content

- [Description](#description)
- [Deployed website link](#deployedWebsite)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contribution)
- [Tests](#tests)
- [GitHub](#github)
- [Contact](#contact)
- [License](#license)




![GitHub repo size](https://img.shields.io/github/repo-size/blockchaincyberpunk1/mean_reversion_bot?style=plastic)

  ![GitHub top language](https://img.shields.io/github/languages/top/blockchaincyberpunk1/mean_reversion_bot?style=plastic)



## Description

  The Mean Reversion Trading Bot is a Python-based bot designed to trade assets that deviate significantly from their historical average price. It uses mean-reversion strategy and relies on Python, Pandas, NumPy, Alpaca for trading, and Alpha Vantage for historical data. This bot aims to bet on a return to the mean when assets' prices deviate too far from their historical averages.





<p align="center">
  <img alt="Mean Reversion Trading Bot" [Screenshot] src="python-trading-bot.jpg"><br>
Mean Reversion Trading Bot
</p>





## Installation

Prerequisites:

Python
Python virtual environment
API keys for Alpaca and Alpha Vantage

Clone this repository to your local machine:

git clone https://github.com/blockchaincyberpunk1/mean_reversion_bot.git
cd trading-bot

Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install the required Python packages:

pip install -r requirements.txt

Create a .env file in the project directory and add your API keys:

ALPACA_API_KEY=your_alpaca_api_key
ALPACA_API_SECRET=your_alpaca_api_secret
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key

Replace your_alpaca_api_key, your_alpaca_api_secret, and your_alpha_vantage_api_key with your actual API keys.

Start the trading bot:

python main.py




Mean Reversion Trading Bot is built with the following tools and libraries: <ul><li>Pandas: A powerful data manipulation and analysis library used for handling and analyzing historical price data.</li> <li>NumPy: A library for numerical computations, used for mathematical operations and calculations in the bot.</li> <li>Alpaca: An API for algorithmic trading, used for executing buy and sell orders in the stock market.</li> <li>Alpha Vantage: An API for retrieving historical financial data, used for obtaining historical price data for assets.</li></ul>





## Usage
 
To use the trading bot, follow these steps:

Input your desired trading symbol in the symbol variable inside the main.py script.

Define your trading logic within the mean_reversion_strategy function in the main.py script. You can customize this function based on your strategy.

Run the bot using python main.py. It will continuously monitor the asset's price and execute trades according to your logic.





## Contribution
 
Contributions to this project are welcome! If you would like to contribute, feel free to open issues, submit pull requests, or make suggestions for improvements.





## Tests
 
Testing the trading bot requires a paper trading account on Alpaca. Before running the bot with real funds, it's essential to thoroughly test it with paper trading.





## GitHub

<a href="https://github.com/blockchaincyberpunk1"><strong>blockchaincyberpunk1</a></strong>



<p>Visit my website: <strong><a href="http://blockchaincyberpunk1.github.io/thepolyglot">The Polyglot</a></strong></p>





## Contact

Feel free to reach out to me on my email:
thepolyglot8@gmail.com





## License

[![License](https://img.shields.io/static/v1?label=Licence&message=MIT&color=blue)](https://opensource.org/license/MIT)


