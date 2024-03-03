import requests
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import pandas as pd
import time

# Definicja stałych
MY_LAT = 51.1000000 # Twoja szerokość geograficzna
MY_LONG = 17.0333300 # Twoja długość geograficzna

# Funkcja do pobierania hasła z pliku CSV
def get_email_password():
    app_password = pd.read_csv("../../passwords.csv")
    return app_password.iloc[0, 1]

# Funkcja do wysyłania e-maila
def send_email(sender_email, password, receiver_email):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Spójrz w górę"
    message.attach(MIMEText("Spójrz w górę", "plain", "utf-8"))

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.send_message(message)

# Sprawdzanie pozycji ISS i porównywanie jej z aktualną pozycją
def check_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return iss_latitude >= MY_LAT - 5 and iss_latitude <= MY_LAT + 5 and iss_longitude >= MY_LONG - 5 and iss_longitude <= MY_LONG + 5

# Pobieranie czasu wschodu i zachodu słońca
def get_sunrise_sunset_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    return sunrise, sunset

#Główna funkcja programu
def main():
    while True:
        iss_position_check = check_iss_position()
        time_now = datetime.now()
        sunrise, sunset = get_sunrise_sunset_time()

        if iss_position_check and (time_now.hour >= sunset or time_now.hour <= sunrise):
            send_email("natalia.jasiczak96@gmail.com", get_email_password(), "natalia.jasiczak96@gmail.com")

        time.sleep(60)

if __name__ == "__main__":
    main()
