import requests
import json
from datetime import datetime

def get_gas_price():
    response = requests.get('https://www.gasnow.org/api/v3/gas/price')
    data = json.loads(response.text)
    gas_price = data['data']['standard']
    return gas_price

def save_gas_price_to_github(gas_price):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('gas_price_history.txt', 'a') as file:
        file.write(f'{timestamp}: {gas_price} Gwei\n')

gas_price = get_gas_price()
save_gas_price_to_github(gas_price)

