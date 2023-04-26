k=0
minn=float('inf')
with open('13.txt') as f:
    sp=[int(x) for x in f]
for i in range(len(sp)-1):
    if abs(sp[i])%8==0 and sp[i+1]%8==0:
        k+=1
        minn=min(minn, sp[i]+sp[i+1])
print(k, minn)
print((~18 | (132>> 2)) & (86 << 1))
