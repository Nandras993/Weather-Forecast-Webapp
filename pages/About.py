import streamlit as st
from message import send_mail

st.set_page_config(page_title="About",
                   layout="wide")

st.markdown(body="<h1 style='text-align: center; color: white;'>About</h1>",
            unsafe_allow_html=True)
st.markdown(body="<h5 style='text-align: left; color: white;'>This is a webapp that helps you determine the the weather in the upcoming 5 days by giving it the name of your city/town etc. I created this app with Python, using streamlit and a weather API.</h5>",
            unsafe_allow_html=True)
st.markdown(body="<h5 style='text-align: left; color: white;'>The weather data is updated every 3 hour. <br><br> I used OpenWeather's weather API for this . <br><br> You can visit their website here:</h5>",
            unsafe_allow_html=True)
st.markdown(body="<h3 style='text-align: left; color: white;'><p><a href='https://openweathermap.org/' title='title'>OpenWeatherMap</a></p></h3>",
            unsafe_allow_html=True)
st.markdown(body="<h5 style='text-align: left; color: white;'>If you are curious abot my other works, visit my github page: <br><br><p><a href='https://github.com/Nandras993' title='title'>GitHub</a></p></h5>",
            unsafe_allow_html=True)
st.markdown(body="<h5 style='text-align: left; color: white;'>My LinkedIn: <br><br><p><a href='www.linkedin.com/in/andrás-nagy-20b545244' title='title'>LinkedIn</a></p></h5>",
            unsafe_allow_html=True)

st.markdown(body="<h5 style='text-align: left; color: white;'>If you have any questions, you can send me an email here: <br></h5>",
            unsafe_allow_html=True)

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")
    message = f"""\

From: {user_email}

{raw_message}
"""
    button = st.form_submit_button("Submit")
    print(button)
    if button:
        send_mail(message)
        st.info("Your email message was sent")