#!/usr/bin/python
#-*- utf-8 -*-
import requests
import json
#url='http://www.cntour.cn/'
#strhtml=requests.get(url)
#print(strhtml.text)
#def get_data(word):
 #   url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
  #  form_data=json.dumps({'i': word,
#'from': 'AUTO',
#'to': 'AUTO',
#'smartresult': 'dict',
#'client': 'fanyideskweb',
#'salt': '15639500511598',
#'sign': '70887401b946179e9c42c6ced25a272f',
#'ts': '1563950051159',
#'bv': 'c4e95e621267f4d4577f554f2869b772',
#'doctype': 'json',
#'version': '2.1',
#'keyfrom': 'fanyi.web',
#'action': 'FY_BY_CLICKBUTTION'})

 #   response=requests.post(url,data=form_data)
  #  content=json.loads(response.text)
   # print(content)
#if __name__=='__main__':
 #   get_data('我爱中国')

#url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd={}.format(传智播客)'
url='https://www.biqukan.com/1_1094/5403177.html'
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
r=requests.get(url=url,headers=headers)
print(r.status_code)
print(r.request.url)
print(r.request.headers)
print(r.text)




