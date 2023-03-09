import requests

headers = {'Authorization': 'Bearer a26dd88cf63765cb7b1a0b247fc6ce48b66a64f2'}

product_title = input('enter title of product to add\n')
product_content = input('enter content of product to add\n')
product_price = input('enter price of  new product\n')
product_price = int(product_price)

endpoint = 'http://localhost:8000/api/products/'

data = {
    'title': f'{product_title}',
    'content': f'{product_content}',
    'price': f'{product_price}'
}
get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())
