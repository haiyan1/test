#!/user/bin/python
#coding:utf-8
from operator import pos
import requests
import json
url='http://10.8.40.233:8089/SMSService/verificationCode'
data1=json.dumps({
    'user_name': 'YWRtaW4=',
    'user_pwd': 'ZTEwYWRjMzk0OWJhNTlhYmJlNTZlMDU3ZjIwZjg4M2U=',
    'date': '2016-12-01 13:24:23'
})
r=requests.post(url,data=data1)
print (r.json())
print (r.json()['verCode'])


url2='http://10.8.40.233:8089/SMSService/user_register'#接口地址


data11=json.dumps({
    'operator':'ggzb',
    'userId':'12345600',
    'deviceSN':'3456789',
    'registerDate':'2017-01-22 10:09:51',
    'verCode':r.json()['verCode']
})

# 这个data是固定的
r2=requests.post(url2,data=data11)
print (r2.json())

