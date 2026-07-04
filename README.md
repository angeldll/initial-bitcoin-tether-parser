# Bitcoin Rate Parser

A simple Python script that fetches current Bitcoin and Tether rates from the CoinGecko API and saves them to a JSON file.

## Features
- Gets BTC and USDT rates in USD, EUR, RUB
- Saves data to `rate.json` in a pretty format
- Checks HTTP status before parsing
- Handles connection errors gracefully

## Technologies
- Python 3
- `requests` library
- CoinGecko API (free, no API key required)

## How to Run
1. Install dependencies: `pip install requests`
2. Run: `python bitcoin.py` (or whatever you named it)
3. Check `rate.json` for the saved data

## Author
angel.dll, 2026