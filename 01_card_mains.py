
import card_info
while True:
     print("*"*50)
     print("欢迎使用【名片管理系统】")
     print("1.新建名片")
     print("2.显示全部")
     print("3.查询名片")
     print()
     print("0.退出系统")
     print("*"*50)
     r=input("请选择希望执行的操作：")
     print("您选择的操作是：%s"%r)
     if r in ["1","2","3"]:
         if r=="1":
             card_info.new_card()
         elif r=="2":
             card_info.xianshi_card()
         elif r=="3":
             card_info.chaxun_card()
     elif r=="0":
         print("欢迎再次使用【名片管理系统】")
         break
     else:
         print("您输入错误，请重新输入")




