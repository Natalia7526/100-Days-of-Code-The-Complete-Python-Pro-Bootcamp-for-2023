import pandas as pd
import requests


def get_api_key():
    df = pd.read_csv("../../passwords.csv")
    api_key = df[df['name'] == 'open_weather_api_key']['password'].values[0]
    return api_key

def fetch_weather_data():
    api_key = get_api_key()
    omw_endpoint = " https://api.openweathermap.org/data/2.5/forecast"
    parameters = {
        # "lat": 51.1000000,
        "lat": 50.057640,
        # "lon": 17.0333300,
        "lon": 22.489300,
        "appid": api_key,
        "cnt": 4,
    }
    response = requests.get(url=omw_endpoint, params=parameters)
    response.raise_for_status()
    weather_data = response.json()
    return weather_data


def bring_an_umbrella():
    weather_data = fetch_weather_data()
    will_rain = False
    for hour_data in weather_data["list"]:
        condition_code = hour_data["weather"][0]["id"]
        if int(condition_code) < 700:
            will_rain = True
    if will_rain:
        print("Bring an umbrella.")

bring_an_umbrella()

# response = fetch_weather_data()
# weather_id = response.json()["list"][0]["weather"][0]["id"]
# weather_description = response.json()["list"][0]["weather"][0]["description"]
