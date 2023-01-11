#https://kompege.ru/variant?kim=25003483
f=open('27_B_25003483.txt')
n=int(f.readline())
S=0
minr=99999999
for line in f:
    a,b
    a,b
    maxx=max(a,b)
    minn=min(a,b)
    
    S+=maxx
    if (maxx-minn)%3!=0:
        minr=min(minr,maxx-minn)
    
if S%3!=0:
    print(S)
else:
    print(S-minr)
    
