import requests

URL = 'http://127.0.0.1:8000/'

req = requests.get(url= URL)

data_ = req.json()

print(data_)