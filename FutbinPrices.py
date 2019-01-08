import requests  
import json 
import datetime
import time

domain = 'https://www.futbin.com'  
version = 19  
page = 'playerPrices'
old_px = {}
current_px={}
player_id = {
        'Rafinha':201400,
        'Thiago Silva':164240
        }

def fetch_price():
    for (name, id) in player_id.items():
        url = "%s/%s/%s?player=%s" % (domain, version, page, id)
        response = requests.get(url)
        data = response.json()
        current_px[name] = data[str(id)]['prices']['ps']['LCPrice']

fetch_price()
print(current_px, 'Kick off')
for (name, id) in player_id.items():
        old_px[name] = current_px[name]

while True:
        current_time = datetime.datetime.now()
        fetch_price()
        for (name, id) in player_id.items():
                old_price = old_px[name]
                current_price = current_px[name]
                if old_price == current_price:
                        print('-'*60)
                        print('\33[0;37;40m No price updates detected for', name, '=>', current_px, current_time.strftime("%H:%M %Z"))
                else:
                        old_px[name] = current_px[name]
                        print('*'*60)
                        print('\33[1;31;40m Price updates detected for', name, ' from:', old_price, 'to:', current_price, 'at', current_time.strftime("%H:%M %Z"))
        time.sleep(10)
