import requests

TOKEN = "wurwirifslkls"
USERNAME = "natalia7526"

pixela_endpoint = "https://pixe.la//v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# AUTHENTICATION

headers = {
    "X-USER-TOKEN": TOKEN
}

# GRAPH
GRAPH_ID = "booktracker"

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "pages",
    "type": "int",
    "color": "ajisai"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# PIXELS
DATE = "20240312"

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_config = {
    "date": DATE,
    "quantity": "21",
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)