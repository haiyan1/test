import time
a=[]
t0=time.clock()
for i in range(1,20000):
    a.append(i)
print(time.clock()-t0,'seconds process time')

t0=time.clock()
b=[i for i in range(1,20000)]
print(time.clock() - t0,'seconds process time')


d={i:i+1 for i in range(4)}
print(d)
g={i:j for i,j in zip(range(1,6),'abcde')}
print(g)
g={i:j.upper() for i,j in zip(range(1,6),'abcde')}
print(g)


