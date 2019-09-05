import time
file=open("rrr.txt","w")
for i in range (2019081000000000,201908100000003):
    # print(str(i),file=file)
    file.write(str(i))
    file.write("\n")
file.close()
file=open("rrr.txt","r")
while True:
    username=file.readline()
    if not username:
        break
    print(username)

# list.append(username)

print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))




