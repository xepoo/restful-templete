import requests
import json

headers = {'Content-type':'application/json','Accept':'application/json'}
data={"id":"321","name":"test1"}
add_url="http://127.0.0.1:5000/add_name/"
data_json = json.dumps(data)

response = requests.post(add_url, data=data_json, headers=headers)
print(response.text)


get_url="http://127.0.0.1:5000/get_name/"
response = requests.get(get_url, params={'id':321})
print(response.text)

