import requests
import os
from twilio.rest import Client

URL = 'https://api.openweathermap.org/data/2.5/onecall'

account_sid = 'AC246428df933d046c2bea38e6048d4731'
auth_token = '1c7204a3484a153b6b4b04992f3b01b1'

API_KEY = 'e8b44775b4d9f1fe8d1bc327407660c2'
LAT = -26.204103
LON = 28.047304

params = {
    'lat': LAT,
    'lon': LON,
    'appid': API_KEY,
    'exclude': 'current,minutely,daily'
}

response = requests.get(url=URL, params=params)

response.raise_for_status()

weather_data = response.json()

weather_slice = weather_data['hourly'][:12]

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if condition_code < 700:
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body="It's going to rain today. Remember to bring an ☂",
            from_='+12019480624',
            to='+237653346688'
        )
        print(message.status)
        break
