maxx=0
for x in range(1, 1078):
    k0=0
    a=7**77+7**33-x
    while a!=0:
        if a%7==0:
            k0+=1
        a=a//7
    if k0>maxx:
        maxx=k0
        s=x
print(s, maxx)