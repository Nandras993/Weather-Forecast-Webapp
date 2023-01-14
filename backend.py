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
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if type_of_weather == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if type_of_weather == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]

    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Budapest", forecast_days=3, type_of_weather="Sky"))
