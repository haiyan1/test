#-*- coding:utf-8 -*-
import requests
import json
host = "http://httpbin.org/"
endpoint="post"
url=''.jion([host,endpoint])
data={'key1':'value1','key2':'calue2'}

r=requests.post(url,data=data)
#response =r.json()
print(r.test)
