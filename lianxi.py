#数值转换
def shuru(c):
    a=round(c/1000,3)
    return(str(a)+'kg')
m=int(input('请输入g数:'))
tt=shuru(m)
print(tt)


#求平方根
import math
a=int(input('a= '))
b=int(input('b= '))
c=math.sqrt(a*a+b*b)
print('the right triangle third side length is:',c)

#写文件
def text_create(name,msg):
    desktop_path = 'E:/学习/'
    full_path = desktop_path + name +'.txt'
    file = open(full_path,'w')
    file.write(msg)
    file.close()
    print('Done')

text_create('hello','hello world!')


#if ...else
password_list = ['*#*#','12345']
def account_login():
    password = input('Password')
    password_correct = password == password_list[-1]
    password_reset = password == password_list[0]
    if password_correct:
        print('Login success!')
    elif password_reset:
        new_password = input('Enter a new password:')
        password_list.append(new_password)
        account_login()
    else:
        print('Wrong password or invalid input!')
        account_login()
account_login()

#for
songlist = ['Holy Diver','Thunderstruck','Rebel Rebel']
for song in songlist:
    if song=='Holy Diver':
        print(song,'-Dio')
    elif song == 'thunderstrunck':
        print(song,'-AC/DC')
    else:
        print(song,'-David Bowie')



password_list = ['*#*#','12345']
count = 0
def account_login():
    password = input('Password')
    password_correct = password == password_list[-1]
    password_reset = password == password_list[0]
    if password_correct:
        print('Login success!')
    elif password_reset:
        new_password = input('Enter a new password:')
        password_list.append(new_password)
        account_login()
    else:
        print('Wrong password or invalid input!')
        account_login()
        count = count+1
        while count ==3:
            break
account_login()
