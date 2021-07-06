import requests
from requests.api import patch 

response = requests.get('https://api.thecatapi.com/v1/images/search')
print(response)
print(response.status_code)
print(response.content)