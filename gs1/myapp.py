import requests
import json



# URL = 'http://127.0.0.1:8000//student_create/'
# URL = 'http://127.0.0.1:8000//jay_hari/'
URL = 'http://127.0.0.1:8000//om_shree/'

def jay_hari():
  request = requests.get(url=URL, data={})
  response = request.json()
  print("\n\n 🎉 ", response)

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
    'name': 'Ramnath',
    'roll': 21,
    'city': 'Mantha'
  }

  headers = {'content-Type': 'application/json'}

  json_data = json.dumps(data)
  req = requests.post(url = URL, headers=headers, data = json_data)

  data = req.json()
  print('\n\n💥💯🌼 ', data)


def put_data():
  data = {
    'id': 10,
    'name': 'Bhumiti',
    'roll': 57,
    # 'city': 'Mumbai'
  }

  headers = {'content-Type': 'application/json'}

  json_data = json.dumps(data)
  req = requests.put(url = URL, headers=headers, data = json_data)

  data = req.json()
  print('\n\n💥💯🌼 ', data)



def delete_data():
  data = {'id': 16}

  headers = {'content-Type': 'application/json'}

  json_data = json.dumps(data)
  req = requests.delete(url = URL, headers=headers, data = json_data)

  data = req.json()
  print('\n\n  ✨🌹 ', data)




def main():
  # post_data() 
  # put_data() 
  jay_hari()
  # get_data(1)
  # delete_data()
  pass 

if __name__ == '__main__':
  main()