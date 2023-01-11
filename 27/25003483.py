#https://kompege.ru/variant?kim=25003483
f=open('27_B_25003483.txt')
n=int(f.readline())
S=0
minr=99999999
for line in f:
    a,b,c=line.split()
    a,b,c=int(a),int(b),int(c)
    maxx=max(a,b,c)
    minn=min(a,b,c)
    sr=a+b+c-maxx-minn
    S+=maxx
    if (maxx-sr)%109!=0:
        minr=min(minr,maxx-sr)
    elif (maxx-minn)%109!=0:
        minr=min(minr,maxx-minn)
if S%109!=0:
    print(S)
else:
    print(S-minr)
    
