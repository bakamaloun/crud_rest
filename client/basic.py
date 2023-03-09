import requests

endpoint = 'http://localhost:8000/api/'

get_response = requests.post(endpoint, json={'title': 'testing post update'})
print(get_response.json())
