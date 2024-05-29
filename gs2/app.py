import requests
import json

def get_customer_data():
  URL = 'http://127.0.0.1:8000/customer_create/'

  user_data = {
    'name' : 'Shree_Tukoba',
    'email' : 'mauli@tukoba.org',
    'password': 'ShreeTukaram₹652'
  }


  json_data = json.dumps(user_data)

  req = requests.post(url=URL, data=json_data)

  data = req.json()
  print('\n\n💥💯🌼 ', data)




# URL = 'http://127.0.0.1:8000/customer_api/'
URL = 'http://127.0.0.1:8000/customer_class_api/'

def get_data(id =None):
  data = {}
  if id is not None:
    data = {'id': id}
  
  json_data = json.dumps(data)

  req = requests.get(url= URL, data=json_data)

  data = req.json()

  print('\n\n 🔥✨ ', data)


def post_data():
  data = {
    'name': 'Shree_Raghav',
    'email': 'raja2531@yahoo.in',
    'password': 'ga85&*$akjsg'
  }

  json_data = json.dumps(data)

  req = requests.post(url=URL, data=json_data)

  data = req.json()

  print('\n\n 🏋🏻‍♀️🛠🤾🏻‍♂️ ', data)
  
def update_data():
  data = {
    'id': 3,
    'name': 'Radhe_Radhe',
    # 'email': 'radhe1600@radhe.in',
    # 'password': 'radhe85@21₹',
  }

  json_data = json.dumps(data)
  req = requests.put(url=URL, data=json_data)

  res_data = req.json()
  print('\n\n 🎉🤸🏻‍♀️ ', res_data)


def delete_data():
  data = {'id': 2}
  json_data = json.dumps(data)

  req = requests.delete(url=URL, data=json_data)

  res_data = req.json()
  print('\n\n 🔄✨🛠', res_data)

def main():
  get_data(6)
  # post_data()
  # update_data()
  # delete_data()


if __name__ == "__main__":
  main()