import requests
import json

headers = {'Content-type':'application/json','Accept':'application/json'}
data={"id":"321", "name":"test2"}
url="http://127.0.0.1:5000/add_name/"
data_json = json.dumps(data)

response = requests.post(url, data=data_json, headers=headers)
print(response.text)