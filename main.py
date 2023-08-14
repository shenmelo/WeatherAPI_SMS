import requests
from twilio.rest import Client

api_key = "Your API key"
LONGITUDE = -95.992775
LATITUDE = 36.153980
API_ADDRESS = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "ACf0f882f3fee3ea34f344d5246df4c42a"
auth_token = "Your authentication token"

parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(API_ADDRESS, params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False

for entry in data["hourly"][:12]:
    weather = entry["weather"][0]
    weather_id = weather["id"]
    if weather_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+18787887278',
        body='Hello this is python! Weather is not good bring an umbrella☔️.',
        to='+639760151450'
    )
    print(message.status)
