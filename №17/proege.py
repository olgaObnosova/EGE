with open('proege.txt') as f:
    sp=[]
    minn=float('inf')
    maxx = -float('inf')
    for line in f:
        sp.append(int(line))
        if abs(int(line))%100==68:
            minn=min(minn, int(line))
k=0
for i in range(len(sp)-1):
    if ((abs(sp[i])%100==68 and abs(sp[i+1])%100!=68) or \
            ((abs(sp[i]) % 100 != 68 and abs(sp[i + 1]) % 100 == 68))) and \
        sp[i]**2+sp[i+1]**2>=minn**2:
        k+=1
        maxx=max(maxx, sp[i]**2+sp[i+1]**2)
print(k)
print(maxx)

