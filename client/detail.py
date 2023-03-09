import requests

product_id = input('enter id of product to see Details of\n')
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} is not valid')

if product_id:
    endpoint = f'http://localhost:8000/api/products/{product_id}/'

get_response = requests.get(endpoint)
print(get_response.json())
