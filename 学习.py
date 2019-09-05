#!/usr/bin/python
#-*-coding:UTF-8-*-

#输入一个整数求和
sum=0
n=int(input("请输入整数："))
for i in range(n+1):
    sum=sum+i
print(sum)

def hanoti(n,x1,x2,x3):
    if(n == 1):
        print('move:',x1,'-->',x3)
        return
    hanoti(n-1,x1,x3,x2)
    print('move:',x1,'-->',x3)
    hanoti(n-1,x2,x1,x3)

hanoti(4,'A','B','C')



numbers =[12,37,5,42,8,3]
even=[]
odd=[]
while len(numbers)>0:
    number =numbers.pop()
    if(number % 2==0):
        even.append(number)
    else:
        odd.append(number)

print ('even=',even)
print('odd=',odd)


for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print ('%d 等于 %d * %d' % (num,i,j))
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print (num, '是一个质数')



for i in range(1,11):
    for j in range(1,i):
        print (j),


arays = [1,8,2,6,3,9,4]
for i in range(len(arays)):
    for j in range(i):
        if arays[i] < arays[j]:
            # 实现两个变量的互换
            arays[i],arays[j] = arays[j],arays[i]
print (arays)

str=input("请输入：")
print("你输入的内容是：",str)


sum=0
for i in range(1,101):
    print(sum=sum+i)
