#！/usr/bin/python
#-*-coding:UTF-8 -*-
class Employee:
    empCount = 0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount +=1

   # def displayCount(self):
   #     print("total employee %d" %Employee.empCount)
    def displayEmployee(self):
        print("Name:",self.name,"salary:",self.salary)
aa1=Employee("Zara",2000)
bb2=Employee("Manni",5000)
aa1.displayEmployee()
bb2.displayEmployee()
print('the total %d'% Employee.empCount)

for i in range(1,10):
    for j in range(1,i+1):
        print ('%d*%d=%d'%(i,j,i*j),end=' ')
    print('\n')

for n in range(100,1000):
    l=n//100
    m=n//10%10
    k=n%10
    if (n==l**3+m**3+k**3):
        print(n)



import _thread
import time
def print_time(threadName,delay):
    count=0
    while count<5:
        time.sleep(delay)
        count +=1
        print ("%s:%s"%(threadName,time.ctime(time.time())))
try:
    _thread.start_new_thread(print_time,("Thread-1",1,))
    _thread.start_new_thread(print_time,("Thread-2",1,))
except:
    print ("Error:unable to start thread")
while 1:
    pass




