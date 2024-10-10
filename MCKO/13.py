with open('13.txt') as f:
    sp=[int(x) for x in f]
k=0
minn=float('inf')
for i in range(len(sp)-1):
    if abs(sp[i])%8==0 and abs(sp[i+1])%8==0:
        k+=1
        minn=min(minn, sp[i]+sp[i+1])
print(k, minn)
