#coding:utf-8
#同种类型可以相加
num=1
string='1'
num2 = int(string)
print(num + num2)

#字符串之间相乘
words='words '*3
print(words)

word = 'a loooooong word'
num = 12
string = 'bang! '
total = string*(len(word)-num)
print(len(word)-num)
print(total)


print('sdhfjksdhfjksdhf\
dfddfdfdffddfdfdfdfdfdffdfdfdfddfadf\
    dfsdfdfdf')

phone_number='138-0098-9999'
hiding_number=phone_number.replace(phone_number[:9],'*'*9)
print(hiding_number)
search='138'
print(search + ' is at ' + str(phone_number.find(search)+1))

#创建10个空文件
def create_txt(t):
    for name in range(1,t):
        f_path='E:/学习/'
        full_path=f_path + str(name) +'.txt'
        file_name=open(full_path,'w')
create_txt(11)

#计算复利息
import math
def invest(amount,rate,time):
    print('principal amount:',amount)
    #if time==1:
        #print('year 1:$',amount*((1+rate)))
    #elif time >1:
    for i in range(1,time):
        print('year ',i,':$',amount*pow((1+rate),i+1))
invest(100,0.05,8)

#打印1~100内的偶数
def odd(t):
    for i in range(1,t):
        if i%2==0:
            print(i)
odd(10)



#摇骰子比大小
import random
def ss():
    n=input('please input big or small :')
    L = []
    for i in range(3):
        point1=random.randrange(1,6)
        L.append(point1)
        tt=sum(L)
    if 11<=tt<=18:
            m='big'
            if m==n.lower():
                print('the points are', L, 'You Win!')
            else:
                print('the points are',L,'You Lose!')
    elif 3<=tt<=10:
            m='small'
            if m==n.lower():
                print('the points are',L,'You win!')
            else:
                print('the points are',L,'You Lose!')
ss()



#判断输入的手机号码是否合法
CN_mobile=['134','135','136','137','138','139','150','151','152','157','158',
           '159','182','183','184','187','188','147','178','1705']
CN_union=['130','131','132','155','156','185','186','145','176','1709']
CN_telecom=['133','153','180','181','189','177','1700']
def yanzhengma():
    t=input('Enter your number:')
    if len(t)<11 :
        print('Invalid length,your number should be in 11 digits')
    elif len(t)==11:
        if str(t)[0:3] in CN_mobile:
            print('Operator:China mobile')
            print('We\'re sending verification code via text to your phone:', t)
        elif str(t)[0:3] in CN_telecom:
            print('Operator:China telecom')
            print('We\'re sending verification code via text to your phone:', t)
        elif str(t)[0:3] in CN_union:
            print('Operator:China union')
            print('We\'re sending verification code via text to your phone:', t)
        else:
            print('No such a operator')
    else:
        print('Invalid length,your number should be in 11 digits')

yanzhengma()




