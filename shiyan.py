#!/usr/bin/python

# -*- coding: UTF-8 -*-

import requests

import unittest
import json
class TestDemo(unittest.TestCase):
def setUp(self):
   pass

 def test_Demo1(self):

  xmlhead = xxxxxx

  xmlbody = xxxxxx

  data = {'xmlhead' : xmlhead, 'xmlbody' : xmlbody} #xmlhead、xmlbody为xml格式的报文头、报文体

  url = 'http://xxxxxx'

  result = requests.post(url,data=data)

  try:
    self.assertEqual(result.status_code, 200)
    print ("用例测试通过")
  except Exception as e:
      print (e)
      print ("用例测试不通过")  #之前写的是格式为print (e, '用例测试不通过')，打印出来的语句非utf-8格式，因此在此写了两个print

 def tearDown(self):
  pass

if __name__ == '__main__':
   unittest.run()
import xlrd
class ReadXml(object):
def __init__(self,path = ''):
   self.url = xlrd.open_workbook(path) #打开文件


def get_Datasheet_by_name(self,sheet):
   self.sheet = self.url.sheet_by_name(sheet) #获取sheet页的名字
   return self.DataList()


def DataList(self):
    list = []
   for row in range(0, self.sheet.nrows): #nrows()方法为获取某一sheet页的行数
     resu = self.sheet.row_values(row) #row_values()批量获取单元格数据
    list.append(resu)
   return list

import read_excal

def get_data(self,sheet,row,col):

  filepath = read_excal.ReadXml('D:\xx\xx\\xx.xlsx')  #在具体文件名前面可以加‘\’，但在本地运行时有时加一个'\'保存，所以加了'\\'确保程序正常运行

  ResultData = filepath.get_Datasheet_by_name(sheet)

  return ResultData

import requests
import unittest
import base #导入base模块
class TestDemo(unittest.TestCase):
  def setUp(self):
    self.xmlhead = base.get_data('xmlhead')  #读取'xmlhead'页的所有数据
    self.xmlbody = base.get_data('xmlbody')  #读取'xmlbody'页的所有数据
  def test_Demo1(self):
    xmlhead = self.xmlhead[0][0]     #获取'xmlhead'页的第1行第1列数据
    xmlbody = self.xmlbody[13][1]    #获取'xmlbody'页的第14行第2列数据
    data = {'xmlhead' : xmlhead, 'xmlbody' : xmlbody}  #xmlhead、xmlbody为xml格式的报文头、报文体
