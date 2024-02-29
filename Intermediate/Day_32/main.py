import random
import smtplib
import pandas as pd
import datetime as dt
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt", "r", encoding="utf-8") as quotes:
        lines = quotes.readlines()
        random_quote = random.choice(lines)

    my_email = "natalia.jasiczak96@gmail.com"
    app_password = pd.read_csv("../../passwords.csv")
    password = app_password.iloc[0, 1]

    # Create the message
    message = MIMEMultipart()
    message["From"] = my_email
    message["To"] = "knop.krzysiek@gmail.com"
    message["Subject"] = "Monday motivation"

    # Add the random quote to the message
    message.attach(MIMEText(random_quote, "plain", "utf-8"))

    # Connect to Gmail SMTP server
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.send_message(message)