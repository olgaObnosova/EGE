#https://kompege.ru/variant?kim=25003645
f=open('27b25003645.txt')
n=int(f.readline())
a=[]
s=0
Sum=0
minn=9999999
MIN=999999
for line in f:
    line=int(line)
    while line%2!=0:
        a.append(line)
        line=int(f.readline())       
    a.sort()
    '''
    if len(a)>2 and (a[1]-a[0])!=0:
        minR=min(minR,a[1]-a[0])
    elif len(a)==1:
        minR=min(minR,line)
    '''
    a.append(line)
    for x in a:
        if x%2!=0:
            minn=min(minn,x)
    s=sum(a)
    if s%2!=0 and minn!=9999999:
        s=s-minn
    Sum+=s
    MIN=min(minn,MIN)
    if line%10!=0:
        MIN=min(MIN,line)
    #print(a)
    a=[]
    minn=9999999
print(Sum, MIN)
print(Sum-MIN)
