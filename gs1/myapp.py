import requests
import json



URL = 'http://127.0.0.1:8000//student_create/'


data = {
  'name': 'Jay Hari',
  'roll': 18501,
  'city': 'Alandi'
}

json_data = json.dumps(data)
req = requests.post(url = URL, data = json_data)

data = req.json()
print('\n\n💥💯🌼 ', data)