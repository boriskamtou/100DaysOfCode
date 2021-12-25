from datetime import datetime

import requests

USERNAME = 'boriskamtou'
TOKEN = 'thisismysecrettoken123'
GRAPH_ID = 'graph1'
pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
# TODO 1: create user account with POST REQUEST
# # When we want to make a POST request, instead of 'params' property
# # we use json
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.json())

# Create a graph
graphs_url = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    'X-USER-TOKEN': TOKEN,
}

create_graph_params = {
    'id': GRAPH_ID,
    'name': 'Cycling graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'shibafu',
}
response = requests.post(url=graphs_url, json=create_graph_params, headers=headers)

# CREATE pixel
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
data = {
    'date': today.strftime('%Y%m%d'),
    'quantity': '25',
}
res = requests.post(url=post_pixel_endpoint, json=data, headers=headers)
print(res.text)

# UPDATE pixel
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
update_params = {
    'quantity': '50'
}
result = requests.put(url=update_pixel_endpoint, json=update_params, headers=headers)
print(result.text)

# DELETE pixel
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
result = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(result.text)
