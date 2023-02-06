import smtplib
import json
from email.message import EmailMessage
import streamlit as st

path = "configuration.json"

with open(path, "r") as handler:
    info = json.load(handler)

sender = st.secrets("username")
password = st.secrets("password")
receiver = st.secrets("username")


def send_mail(message):
    print("send_email function started")
    email_message = EmailMessage()
    email_message["Subject"] = "Contact from Weather Forecast Webapp!"
    email_message.set_content(message)

    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login(user=sender, password=password)
    mail.sendmail(sender, receiver, email_message.as_string())
    mail.quit()
    print("send_email function ended")


if __name__ == "__main__":
    send_mail()
