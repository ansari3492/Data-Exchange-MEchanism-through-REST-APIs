# -*- coding: utf-8 -*-
"""
Created on Thu May 17 12:34:35 2018

@author: Lenovo
"""






import requests
url2 = 'http://13.127.155.43/api_v0.1/sending'
payload = {'Phone_Number' : '9783183918','Name' : 'Mohammed Burhan','Branch' : 'B.Tech CSE',
'College_Name' : 'Bmit'}

# GET
r = requests.get(url2)
# POST with form-encoded data
r = requests.post(url2, json=payload)
print (r.text)
# POST with JSON 
import json
r = requests.post(url2, data=json.dumps(payload))

url1 = 'http://13.127.155.43/api_v0.1/receiving?Phone_Number=9783183918'
# GET
r = requests.get(url1)
print (r.text)