API_KEY = "b74a0732-e4a1-4067-841d-3ab9f0e421e3"

header = {
            'X-CMC_PRO_API_KEY': API_KEY,
            "Accept": "application/json"
        }

params = {
            'start': '1',
            'limit': '20',
            'convert': 'USD',
        }

LATEST_TOP_LISTING_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

COIN_MARKET_API_DOMAIN = "https://api.coingecko.com/api/v3/"

CURRENCY_LIST = {
    "USD",
    "INR"
}


