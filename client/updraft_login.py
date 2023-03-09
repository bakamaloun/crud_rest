import requests
from getpass import getpass

auth_endpoint = 'http://getupdraft.com/api/user/login/'
username = 'korepanov@moqod.com'
password = '1234Qwer!'

auth_response = requests.post(auth_endpoint, data=None, json={'username': username, 'password': password})
print(auth_response.json())

