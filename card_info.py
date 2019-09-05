# 1、定义一个list列表
card_list = []

#1.新增名片
def new_card():
    print("-"*50)
    print("1.新增名片")
    #2、输入的信息
    name = input("请输入姓名：")
    qq = input("请输入qq：")
    tel = input("请输入电话：")
    email = input("请输入邮箱：")
    #3、定义字典，将输入的信息存放到字典中
    card_dict={"name":name,"qq":qq,"tel":tel,"email":email}
    #4、将字典数据存放到list中
    card_list.append(card_dict)
    #5、输出list列表
    print(card_list)
    print("信息添加成功%s"%card_dict["name"])

def xianshi_card():
    print("-"*50)
    print("【显示所有的名片】")
    #1、如果列表为空即长度为0，则返回
    if len(card_list)==0:
        print("名片信息为空")
        return
    #2、不满足1，继续向下执行，显示title
    for name in ["姓名","qq","电话","邮箱"]:
        print(name,end="\t\t")
    print("")
    #3、循环显示列表中的内容
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s"%(card_dict["name"],card_dict["qq"],card_dict["tel"],card_dict["email"]))


def chaxun_card():
    print("-"*50)
    print("搜索名片")
    find_name=input("输入查询的名字：")
    for card_dict in card_list:
        if find_name ==card_dict["name"]:
            print(card_dict)
            break
    else:
        print("没有查询到相应的信息")


