import json
import requests

path = "configuration.json"

with open(path, 'r') as handler:
    info = json.load(handler)

API_KEY = info["API_KEY"]


def get_data(place, forecast_days=None, type_of_weather=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data


if __name__ == "__main__":
    print(get_data(place="Tokyo"))
