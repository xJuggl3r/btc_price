Bitcoin Price Notifier
Introduction
This project is a python script that tracks the price of Bitcoin and sends notifications when the price is below a specified threshold or every 5 minutes (depending on the implementation). The notifications are sent through the IFTTT Webhook.

Requirements
The following packages need to be installed:

requests
time
datetime
How it works
The script does the following steps:

Retrieves the current price of Bitcoin from the Binance API
Checks if the price is below the specified threshold. If yes, it sends an emergency notification.
If there are 5 items in the history of bitcoin prices, it sends an update notification with a formatted message.
Sleeps for 5 minutes (can be changed for testing purposes) and repeats the process.
Configuration
You can set the following variables in the code:

BITCOIN_PRICE_THRESHOLD: The threshold value for the price of Bitcoin. When the price is below this value, an emergency notification will be sent.
BITCOIN_API_URL: The URL of the Binance API used to retrieve the price of Bitcoin.
IFTTT_WEBHOOK_URL: The URL of the IFTTT Webhook used to send the notifications.
Usage
To run the script, simply run the main() function.