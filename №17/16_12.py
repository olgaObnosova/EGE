with open('17.txt') as f:
    sp=[]
    maxx=-float('inf')
    for line in f:
        sp.append(int(line))
        if len(str(abs(int(line))))==5 and abs(int(line))%10==3:
            maxx=max(maxx, int(line))
print(maxx)
ms=-float('inf')
cnt=0
for i in range(len(sp)-2):
    k=0
    if abs(sp[i])%10==3:
        k+=1
    if abs(sp[i+1])%10==3:
        k+=1
    if abs(sp[i+2])%10==3:
        k+=1
    if k>0 and (sp[i]+sp[i+1]+sp[i+2])<=maxx:
        cnt+=1
        ms = max(ms, sp[i]+sp[i+1]+sp[i+2])
print(ms,cnt)
