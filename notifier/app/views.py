from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests
from django.views import View

BITCOIN_USD_API_URL = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
BITCOIN_BRL_API_URL = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCBRL'


class BitcoinPriceView(View):
    def get(self, request):

        # Get the current price of bitcoin in USD from the Binance API
        response = requests.get(BITCOIN_USD_API_URL)
        response_json = response.json()
        bitcoin_usd_price = float(response_json['price'])

        # Get the current price of bitcoin in BRL from the Binance API
        response = requests.get(BITCOIN_BRL_API_URL)
        response_json = response.json()
        bitcoin_brl_price = float(response_json['price'])

        return render(request, 'bitcoin_price.html', {'bitcoin_usd_price': bitcoin_usd_price, 'bitcoin_brl_price': bitcoin_brl_price})
