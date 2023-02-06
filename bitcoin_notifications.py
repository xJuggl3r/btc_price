# Description: This is the main file for the project. It will be used to run the program.

import requests
import time
from datetime import datetime

BITCOIN_PRICE_THRESHOLD = 10000  # Set this to whatever you like

BITCOIN_API_URL = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
IFTTT_WEBHOOK_URL = 'https://maker.ifttt.com/trigger/test_event/json/with/key/bkt0ZFdveTtSRR16PnAqH4'


# This function will get the current price of bitcoin from the Binance API
def getBitcoinPrice():
    # Get the current price of bitcoin from the Binance API
    response = requests.get(BITCOIN_API_URL)
    response_json = response.json()
    return float(response_json['price'])

# This function will send a notification to the IFTTT Webhook


def post_ifttt_webhook(event, value):
    # Send a HTTP POST request to the IFTTT Webhook URL
    data = {'value1': value}
    ifttt_event_url = IFTTT_WEBHOOK_URL.format(event)
    requests.post(ifttt_event_url, json=data)

# This function will format the bitcoin history into a nice message


def format_bitcoin_history(bitcoin_history):
    rows = []
    for bitcoin_price in bitcoin_history:
        # Formats the date into a string: '24.02.2018 15:09'
        date = bitcoin_price['date'].strftime('%d.%m.%Y %H:%M')
        price = bitcoin_price['price']
        # <b> (bold) tag creates bolded text
        # 24.02.2018 15:09: $<b>10123.4</b>
        row = '{}: $<b>{}</b>'.format(date, price)
        rows.append(row)

    # Use a <br> (break) tag to create a new line
    # Join the rows delimited by <br> tag: row1<br>row2<br>row3
    return '<br>'.join(rows)


# This function will get the current price of bitcoin and send a notification if the price is lower than the threshold

def main():
    bitcoin_history = []
    while True:
        price = getBitcoinPrice()
        date = datetime.now()
        bitcoin_history.append({'date': date, 'price': price})

        # Send an emergency notification
        if price < BITCOIN_PRICE_THRESHOLD:
            post_ifttt_webhook('bitcoin_price_emergency', price)

        # Send a Telegram notification
        # Once we have 5 items in our bitcoin_history send an update
        if len(bitcoin_history) == 5:
            post_ifttt_webhook('bitcoin_price_update',
                               format_bitcoin_history(bitcoin_history))
            # Reset the history
            bitcoin_history = []

        # Sleep for 5 minutes
        # (For testing purposes you can set it to a lower number)
        time.sleep(5 * 60)
