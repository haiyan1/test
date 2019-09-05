
#sorted 排序，默认升序   reverse=True 降序
name={"name":"xiaoming"}
age={"age":18}
name.update(age)
print(name)


a=[1,5,7,9]
b=[2,2,6,8]
a.extend(b)
print(sorted(a))
print(sorted(a,reverse=True))

def fn():
    try:
        for i in range(5):
            if i>2:
                raise Exception("数字大于2了")
    except Exception as ret:
        print(ret)
fn()

dic={"name":"zs","age":18}
# dic.pop("name")
# print(dic)
del dic["name"]
print(dic)