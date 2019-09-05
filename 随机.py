
import random
num = int(input("请选择（1）石头，（2）剪刀，（3）布:"))
computer = random.randint(1,3)

""" 
1胜2 2胜3 3胜1
"""

if ((num==1 and computer==2)
        or (num==2 and computer==3)
        or (num==3 and computer==1)):
    print("玩家出:%d，电脑出:%d,玩家获胜"%(num,computer))
elif (num==computer):
    print("玩家出:%d，电脑出:%d,平局"%(num,computer))
else:
    print("玩家出:%d，电脑出:%d,电脑获胜"%(num,computer))


