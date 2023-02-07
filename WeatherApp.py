import streamlit as st
import plotly.express as px
from backend import get_data

st.set_page_config(page_title="Weather Forecast",
                   layout="wide")
# Add title, text input, slider, selectbox and subheader
st.markdown(body="<h1 style='text-align: center; color: white;'>Weather Forecast for the Upcoming Days</h1>",
            unsafe_allow_html=True)

st.markdown(body="<h4 style='text-align: center; color: white;'>Welcome to my Weather Forecast Webapp!"
                 " You can see weather data for the upcoming 5 days with 3 hour intervals. If you have any question, "
                 "click the little arrow on the top left of the page, click on About and send me an email.</h4>",
            unsafe_allow_html=True)
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1,
                 max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Weather", "Humidity and Pressure", "Wind"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Get the temp/sky data
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            temp_feel = [dict["main"]["feels_like"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create a temp plot
            col0, col1, col2, col3 = st.columns([0.1, 0.8, 0.1, 1])
            with col0:
                st.markdown("")

            with col1:
                st.write("Temperature:")
                figure = px.line(x=dates, y=temperatures,
                                 labels={"x": "Date", "y": "Temperature (°C)"})
                st.plotly_chart(figure)

            with col2:
                st.markdown("")

            with col3:
                st.write("What it feels like:")
                figure = px.line(x=dates, y=temp_feel,
                                 labels={"x": "Date", "y": "Feels like (°C)"})
                st.plotly_chart(figure)

        if option == "Weather":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            sky_description = [
                f"{dict['weather'][0]['description']} {dict['dt_txt']} -----({dict['main']['temp']}°C)-----"
                for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            print(sky_conditions)
            print(sky_description)
            st.image(image_paths, width=115, caption=sky_description)

        if option == "Humidity and Pressure":
            humidity = [dict['main']['humidity'] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            pressure = [dict['main']['pressure'] / 1000 for dict in filtered_data]

            col0, col1, col2, col3 = st.columns([0.1, 0.8, 0.1, 1])
            with col0:
                st.markdown("")
            with col1:
                st.write("Humidity:")
                figure_hum = px.bar(x=dates, y=humidity,
                                    labels={"x": "Dates", "y": "Humidity (%)"})
                st.plotly_chart(figure_hum)
            with col2:
                st.markdown("")

            with col3:
                st.write("Pressure:")
                figure_press = px.line(x=dates, y=pressure,
                                       labels={"x": "Dates", "y": "Pressure (bar)"})
                st.plotly_chart(figure_press)

        if option == "Wind":
            dates = [dict["dt_txt"] for dict in filtered_data]
            wind_speed = ([dict['wind']['speed'] * 3.6 for dict in filtered_data])
            wind_deg = [dict['wind']['deg'] for dict in filtered_data]
            wind_gust = [dict['wind']['gust'] * 3.6 for dict in filtered_data]
            # wind_description = [f"{dict['dt_txt']} {dict['wind']['speed'] * 3.6}km/h {dict['wind']['deg']}° {dict['wind']['gust'] * 3.6}km/h" for dict in filtered_data]

            print(wind_deg)
            col0, col1, col2, col3 = st.columns([0.1, 0.8, 0.1, 1])

            with col0:
                st.markdown("")

            with col1:
                st.write("Wind speed:")
                figure_ws = px.bar(x=dates, y=wind_speed,
                                   labels={"x": "Dates", "y": "Speed (km/h)"})
                st.plotly_chart(figure_ws)

            with col2:
                st.markdown("")

            with col3:
                st.write("Wind gust:")
                figure_wg = px.bar(x=dates, y=wind_gust,
                                   labels={"x": "Dates", "y": "Speed (km/h)"})
                st.plotly_chart(figure_wg)

    except KeyError:
        name_error = st.warning("The place you entered does not exist. Please enter an existing place!")
