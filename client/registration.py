import requests
from getpass import getpass

reg_endpoint = 'http://localhost:8000/api/register/'

username = input('enter username\n')
password = getpass('enter password\n')
password2 = getpass('enter password2\n')
first_name = input('enter first name\n')
last_name = input('enter last name\n')
email = input('enter email\n')

registration_response = requests.post(reg_endpoint, json={'username': username, 'password': password, 'password2': password2,
                                                 'first_name': first_name, 'last_name': last_name,
                                                 'email': email})
print(registration_response.json())