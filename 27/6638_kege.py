with open('27A_6638.txt') as f:
    n=int(f.readline())
    sp=[]
    for line in f:
        a,b=map(int,line.split())
        sp.append((a,b//100+bool(b%100)))
minn=float('inf')
print(sp)
for i in range(len(sp)):
    s=0
    for j in range(len(sp)):
        s+=abs(sp[i][0]-sp[j][0])*sp[j][1]
    if s<minn:
        minn=s
        otv=sp[i][0]
print(minn, otv)