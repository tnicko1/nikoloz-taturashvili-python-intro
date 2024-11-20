import requests
from datetime import datetime

# CoinGecko API key
API_KEY = 'Use your own API Key' #my API key was here but the code and the Key itself are now deleted


def get_bitcoin_price(date):
    date_obj = datetime.strptime(date, "%Y-%m-%d")

    # Format date is required by CoinGecko API (dd-mm-yyyy)
    formatted_date = date_obj.strftime("%d-%m-%Y")

    url = f"https://api.coingecko.com/api/v3/coins/bitcoin/history?date={formatted_date}"

    headers = {
        'x-cg-demo-api-key': API_KEY
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    if 'market_data' in data:
        price = data['market_data']['current_price']['usd']
        return price
    else:
        return "Price data not available for this date"


date = input("Enter the date (YYYY-MM-DD): ")
price = get_bitcoin_price(date)
if price != "Price data not available for this date":
    paid_price = int(input("How much did you pay at the time? (USD): $"))

    current_date = datetime.now().strftime("%Y-%m-%d")
    current_price = get_bitcoin_price(current_date)
    bitcoin_at_time = paid_price / get_bitcoin_price(date)
    bitcoin_now = paid_price / get_bitcoin_price(current_date)

    bitcoin_difference = bitcoin_at_time - bitcoin_now
    difference_in_usd = bitcoin_difference * current_price

    print(f"bitcoin you got back then: {bitcoin_at_time:.5f} \nbitcoin you would've got now: {bitcoin_now:.5f}\n")

    if bitcoin_difference < 0:
        bitcoin_difference = -bitcoin_difference
        difference_in_usd = -difference_in_usd
        print(f"You lost {bitcoin_difference:.5f} bitcoin, which is equivalent to ${difference_in_usd:.2f} USD")
    elif bitcoin_difference > 0:
        print(f"You profited {bitcoin_difference:.5f} bitcoin, which is equivalent to ${difference_in_usd:.2f} USD")
    else:
        print("Bitcoin values are the same back then and now")
else:
    print(price)
