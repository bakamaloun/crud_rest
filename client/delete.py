import requests

product_id = input('enter id of product to Delete\n')
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} is not valid')
if product_id:
    endpoint = f'http://localhost:8000/api/products/{product_id}/delete/'

    get_response = requests.delete(endpoint)
    print(get_response.status_code)