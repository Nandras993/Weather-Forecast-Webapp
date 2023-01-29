import streamlit as st
from message import send_mail

st.set_page_config(page_title="About",
                   layout="wide")

st.markdown(body="<h1 style='text-align: center; color: white;'>About</h1>",
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