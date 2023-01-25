with open('5789a.txt') as f:
    n, r = map(int, f.readline().split())
    sp=[]
    for line in f:
        line=line.split()
        a=int(line[0])
        b=int(line[1])//50 +bool(int(line[1])%50)
        c=bool(int(line[1])%50)
        sp.append((a,b,c))
print(sp)
maxx=0
for i in range(len(sp)):
    if sp[i][1]>maxx:
        maxx=sp[i][1]
    if sp[i][2]==False:
        print(i)
    s=sp[i][0]
    flag=1
    for j in range(len(sp)):
        if abs(sp[i][0]-sp[j][0])<=r and i!=j and flag:
            if sp[j][2]:
                flag=0
                continue
                s+=sp[j][1]
print(s)
print(maxx)