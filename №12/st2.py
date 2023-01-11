minn=999999
for i in range(201,1000):
    a=i*'1'
    
    while '1111' in a:
        a=a.replace('1111','22',1)
        a=a.replace('222','1',1)
    if a.count('1')<minn:
        minn=a.count('1')
        b=a
        otv=i
print(minn)
print(otv)
