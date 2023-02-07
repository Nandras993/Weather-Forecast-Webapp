import json
import requests
import streamlit as st

path = "configuration.json"

with open(path, 'r') as handler:
    info = json.load(handler)

KEY = {"api": st.secrets["API_KEY"]}

API_KEY = KEY["api"]


def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&units=metric&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Budapest", forecast_days=3))
