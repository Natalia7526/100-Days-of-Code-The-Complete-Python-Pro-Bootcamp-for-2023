import datetime as dt
import random
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_email_password():
    app_password = pd.read_csv("passwords.csv")
    return app_password.iloc[0, 1]

def get_todays_birthdays():
    now = dt.datetime.now()
    day = now.day
    month = now.month

    birthdays = pd.read_csv('birthdays.csv')
    return birthdays[(birthdays['month'] == month) & (birthdays['day'] == day)]

def get_random_letter():
    chosen_letter = "letter_templates/letter_" + str(random.choice([1, 2, 3])) + ".txt"
    with open(chosen_letter, "r") as file:
        return file.read()

def send_birthday_email(sender_email, password, receiver_email, birthday_wishes):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Happy Birthday"
    message.attach(MIMEText(birthday_wishes, "plain", "utf-8"))

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.send_message(message)

def main():
    sender_email = "natalia.jasiczak96@gmail.com"
    password = get_email_password()
    todays_birthdays = get_todays_birthdays()

    for index, row in todays_birthdays.iterrows():
        name = row['name']
        email = row['email']

        birthday_wishes = get_random_letter().replace('[NAME]', name)

        send_birthday_email(sender_email, password, email, birthday_wishes)

if __name__ == "__main__":
    main()
