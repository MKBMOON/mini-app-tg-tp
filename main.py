import requests

TOKEN = '7813747320:AAG7DPyKDs7fivysMVxcMo4TX7TNu1lnR20'
CHAT_ID = '356523865'
URL = 'https://your-mini-app.vercel.app'

message = f'Нажмите на ссылку, чтобы открыть Mini App: {URL}'
url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}'

requests.get(url)