import requests
from datetime import datetime

TOKEN = "wurwirifslkls"
USERNAME = "natalia7526"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ID = "booktracker"


def create_user():
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
    print(response.text)


def create_graph():
    graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
    graph_config = {
        "id": GRAPH_ID,
        "name": "Reading Graph",
        "unit": "pages",
        "type": "int",
        "color": "ajisai"
    }
    headers = {"X-USER-TOKEN": TOKEN}
    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(response.text)


def create_pixel(date, quantity):
    # Format the date into YYYYMMDD
    formatted_date = datetime.strptime(date, "%d/%m/%Y").strftime("%Y%m%d")

    pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
    pixel_config = {"date": formatted_date, "quantity": quantity}
    headers = {"X-USER-TOKEN": TOKEN}
    response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
    print(response.text)


def update_pixel(date, quantity):
    formatted_date = datetime.strptime(date, "%d/%m/%Y").strftime("%Y%m%d")
    pixel_update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}"
    pixel_update_config = {"quantity": quantity}
    headers = {"X-USER-TOKEN": TOKEN}
    response = requests.put(url=pixel_update_endpoint, json=pixel_update_config, headers=headers)
    print(response.text)


def delete_pixel(date):
    formatted_date = datetime.strptime(date, "%d/%m/%Y").strftime("%Y%m%d")
    pixel_delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}"
    headers = {"X-USER-TOKEN": TOKEN}
    response = requests.delete(url=pixel_delete_endpoint, headers=headers)
    print(response)

# Uncomment to run the desired function
# create_user()
# create_graph()
# create_pixel("03/03/2024", "56")
# update_pixel("03/03/2024", "23")
# delete_pixel("03/03/2024")
