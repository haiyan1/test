print('hello,world!')

file = open('E:/学习/file.txt','w')
file.write('hello,world!')

what_he_does = ' plays '
his_instrument = 'guitar'
his_name = 'Robert Johnson'
artist_intro = his_name + what_he_does + his_instrument
print(artist_intro)

seq='strijjj'
print(''.join(reversed(seq)))


num=[[1,2,3],[4,5,6]]
for i in num:
    print(i)
    for j in i:
        print(j)

import calendar
cal=calendar.month(2018,1)
print (cal)

users ={'A':{'first':'yu',
             'last':'lei',
             'location':'hs',},
        'B':{
            'first':'liu',
            'last':'wei',
            'location':'hs',
        },}
for username,userinfo in users.items():
    print("username",username)
    print("userinfo",userinfo)
    fullname=userinfo['first']+""+userinfo['last']
    print("fullname:"+fullname)
    print("location:"+userinfo['location'])

data=open("D:\data.txt",'w')
for i in range(1):
    print('abc'+str(i)+',',end='',file=data)
   # data.close()

def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print ("函数内 : ", total)
#    return total;


# 调用sum函数
total = sum(10, 20);

#def add(arg1, arg2):
#　total = arg1 + arg2
 #   return total
#print (add(1,2))


#def add(x, y):
# #　z = x + y
#print z
#print （add(x,y)）