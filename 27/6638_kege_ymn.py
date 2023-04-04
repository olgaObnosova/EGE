with open('27B_6638.txt') as f:
    n=int(f.readline())
    sp=[]
    s=summ=0
    for line in f:
        a,b=map(int,line.split())
        sp.append((a,b//100+bool(b%100)))
for i in range(len(sp)):
    s+=abs(sp[0][0]-sp[i][0])*sp[i][1] # сумма если в 0
    summ+=sp[i][1] # сумма всех
print(s)
print(summ)
minn=s
r = 0
lefts = sp[0][1]
pravs = 0
for i in range(1, len(sp)):
    pravs = summ - lefts
    r=abs(sp[i][0]-sp[i-1][0])
    s=s + lefts*r -pravs*r
    lefts += sp[i][1]
    if s<minn:
        minn=s
        otv=sp[i][0]
print(minn, otv)
