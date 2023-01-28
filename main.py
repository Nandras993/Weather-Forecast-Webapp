import streamlit as st
import plotly.express as px
from backend import get_data
from PIL import Image
import glob

st.set_page_config(page_title="Weather Forecast")

# Add title, text input, slider, selectbox and subheader
st.title("Weather Forecast for the Upcoming Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1,
                 max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Weather", "Humidity", "Pressure", "Wind"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Get the temp/sky data
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create a temp plot
            figure = px.line(x=dates, y=temperatures,
                             labels={"x": "Date", "y": "Temperature (°C)"})
            st.plotly_chart(figure)

        if option == "Weather":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            sky_description = [f"{dict['weather'][0]['description']} {dict['dt_txt']} -----{dict['main']['temp']}°C-----"
                               for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            print(sky_conditions)
            print(sky_description)
            st.image(image_paths, width=115, caption=sky_description)

        if option == "Humidity":
            humidity = [dict['main']['humidity'] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure_hum = px.bar(x=dates, y=humidity,
                                labels={"x": "Dates", "y": "Humidity (%)"})
            st.plotly_chart(figure_hum)

        if option == "Pressure":
            pressure = [dict['main']['pressure'] / 1000 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure_press = px.line(x=dates, y=pressure,
                                   labels={"x": "Dates", "y": "Pressure (bar)"})
            st.plotly_chart(figure_press)

        #if option == "Wind":
            #wind_speed = ([dict['wind']['speed'] * 3.6 for dict in filtered_data])
            #wind_deg = [dict['wind']['deg'] for dict in filtered_data]
            #wind_gust = [dict['wind']['gust'] * 3.6 for dict in filtered_data]
            #print(wind_deg)

            #images = ["images_wind/wind_small.png", "images_wind/wind_medium.png", "images_wind/wind_strong.png", "images_wind/wind_hurricane.png"]
            #image_paths = [images[deg] for deg in wind_deg]

            #wind_description = [f"{dict['dt_txt']} {dict['wind']['speed'] * 3.6}km/h {dict['wind']['deg']}° {dict['wind']['gust'] * 3.6}km/h" for dict in filtered_data]

            #image = st.image(image_paths, width=100, caption=wind_description)
    except KeyError:
        name_error = st.warning("The place you entered does not exist. Please enter an existing place!")
