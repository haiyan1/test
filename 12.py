#!/usr/bin/python
#  -*-coding:UTF-8-*-
"""
duohangzhushi
ddddd
ddd
"""
doc = open('C:/Users/Administrator/Desktop/sg11.json', 'w')
doc.write('[')
for i in range(8120078301900000, 8120078301902000):
    print('{"userId":"' + str(i) + '"}' + ',', file=doc)

doc.write(']')

# for j in range(0, 50):
# print('t'+str(j))
