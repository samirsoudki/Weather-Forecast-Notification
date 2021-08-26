import os
api_key = os.environ.get("OWS_API_KEY")
print(api_key)
lat = 55.755825
long = 37.617298
time = 1628679475
part = "current,minutely,daily,alerts"
import requests
import datetime as dt
from twilio.rest import Client
account_sid = "ACc35916683193c0054bc09ddfea632c5c"
auth_token = os.environ.get("AUTH_TOKEN")
print(auth_token)
day = dt.datetime.now()
print(day.utcnow())
response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={long}&exclude={part}&appid={api_key}")
response.raise_for_status()
weather_data = response.json()
data = weather_data.get("hourly")
n = 0
iso_code = []
for _ in range(12):
    data_weather = data[:12][n]["weather"]
    data_2 = data_weather[0]
    final_iso_code = data_2.get("id")
    n += 1
    iso_code.append(final_iso_code)
will_rain = False
for x in iso_code:
    if x <= 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="it will rain take an umbrella.",
        from_='+18508163986',
        to='+9617070288995'
    )

    print(message.sid)








