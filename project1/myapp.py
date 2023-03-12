import requests
import json

URL = 'http://127.0.0.1:8000/'
URL1 = 'http://127.0.0.1:8000/1'
URL2 = 'http://127.0.0.1:8000/create_student/'
URL3 = 'http://127.0.0.1:8000/update_student/'
URL4 = 'http://127.0.0.1:8000/delete_student/'


# for i in range(1,7):
#     r = requests.get(url=URL+str(i))
#     # r = requests.get(url=URL1)  
#     try:
#         print(r.json())
#     except:
#         print('no data found')

obj = {
    'id': 5,
}


obj1 = {
    'name':'azan tariq',
    'roll': 434,
    'city': 'karachi',
}

json_data = json.dumps(obj)

json_data1 = json.dumps(obj1)

# r = requests.put(url=URL3, data=json_data1)
r = requests.get(url=URL2, data=json_data1)

print(r.json())