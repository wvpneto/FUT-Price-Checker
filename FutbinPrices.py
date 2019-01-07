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
    return current_px

fetch_price()
print(current_px, 'Kick off')
old_px = current_px

while True:
    current_time = datetime.datetime.now()
    fetch_price()
    if old_px == current_px:
        print('-'*60)
        print('\33[0;37;40m No price updates detected')
        print(current_px, current_time.strftime("%H:%M %Z"))
    elif old_px != current_px:
        print('*'*60)
        print('\33[1;31;40m Price updates detected. Check list closely!!!!!!!!!!!!!')
        print('*'*60)
        print(current_px,current_time.strftime("%H:%M %Z"))
        old_px = current_px
    time.sleep(3)
