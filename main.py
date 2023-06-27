import  requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "**ovw*r"
TOKEN = "****werfdsf***v"
GRAPH_ID = "graph1"


user_parametr = {
    "token": "****werfdsf***v"
    "username": "**ovw*r",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

# response = requests.post(url=pixela_endpoint, json=user_parametr)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "trainPython",
    "unit": "hour",
    "type": "float",
    "color": "ajisai",
}
headers = {
    "X-USER-TOKEN": TOKEN
}



# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_create_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "2.3",
}

# response = requests.post(url=pixel_create_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "5"
}
response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"


# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
