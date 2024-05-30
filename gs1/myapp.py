import requests
import json



URL = 'http://127.0.0.1:6000//student_create/'

def get_data(id = None):
  data = {}
  if id is not None:
    data = {
      'id': id
    }

  json_data = json.dumps(data)
  req = requests.get(url = URL, data = json_data)

  data = req.json()
  print('\n\n💥💯🌼 ', data)



def post_data():
  data = {
    'name': 'Rajesh',
    'roll': 69,
    'city': 'Mayapur'
  }

  json_data = json.dumps(data)
  req = requests.post(url = URL, data = json_data)

  data = req.json()
  print('\n\n💥💯🌼 ', data)

def main():
  post_data() 
  # get_data(1)
  pass 

if __name__ == '__main__':
  main()