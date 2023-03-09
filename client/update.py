import requests

endpoint = 'http://localhost:8000/api/products/11/update/'

data = {
    'title': 'PUT update',
    'price': 23.00
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())