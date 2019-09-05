# !/usr/bin/python
# *-* coding:utf8 *-*
import requests
import json
import time
# 构造数据
file = open("rrr.txt","w")
for i in range (2019081000000000,2019081000000003):
    # print(str(i),file=file)
    file.write(str(i))
    file.write("\n")
file.close()

file = open("rrr.txt", "r")

while True:
    # 获取验证码
    url = 'http://10.8.40.233:8089/SMSService/verificationCode'  # 获取验证码接口地址
    data1 = json.dumps({
        'user_name': 'YWRtaW4=',
        'user_pwd': 'ZTEwYWRjMzk0OWJhNTlhYmJlNTZlMDU3ZjIwZjg4M2U=',
        'date': '2016-12-01 13:24:23'
    })
    r = requests.post(url, data=data1)
    # 输出结果可以注释掉，调试的时候再打开
    # print(r.json())
    #逐行读取数据
    username = file.readline().split()
    if not username:
        break
    # print(username[0])
    # 将读到的数据传给注册接口
    url2='http://10.8.40.233:8089/SMSService/user_register'#注册接口地址
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    data11=json.dumps({
        'operator': 'ggzb',
        'userId': username[0],
        'deviceSN': '121212',
        'registerDate': date,
        'verCode': r.json()['verCode']
    })
    # 这个data是固定的
    r2=requests.post(url2,data=data11)
    print(r2.json())



