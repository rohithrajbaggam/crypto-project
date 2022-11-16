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


# API_LAYER_API_KEY = "o7PyoG9BsdfZ8OJLsxUGdIkSL2EW8biY" # 19bcs1812@gmail.com
# API_LAYER_API_KEY = "BOFzGqMdAVxVHeUxJ97EPhzcXZzLMhMd" # mantribhanuteja@gmail.com
API_LAYER_API_KEY = "K6RcQx94GZrxxv0O7Jga7RNwBuiq6Q4c" # rohithbaggam.github@gmail.com


APILAYER_API_URL = "https://api.apilayer.com/currency_data/convert?to=INR&from=USD&amount=1"
APILAYER_payload = {}
APILAYER_headers= {
  "apikey": API_LAYER_API_KEY
}
"""
url = "https://api.apilayer.com/currency_data/convert?to=INR&from=USD&amount=1"

payload = {}
headers= {
  "apikey": "o7PyoG9BsdfZ8OJLsxUGdIkSL2EW8biY"
}

"""
