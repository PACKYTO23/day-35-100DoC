import requests

parameters = {
    "lat": 29.072968,
    "lon": -110.955917,
    "appid": "195b62e121233a9ddeffa4adfe6ab458",
    "cnt": 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)

# print(response.status_code)

response.raise_for_status()

weather_data = response.json()

will_rain = False

for forecast in weather_data["weather"]:
    if forecast["id"] < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella!")
