sp=[0]*1001
sp[0]=0
for i in range(1,1001):
    if i%2==0:
        sp[i]=sp[i//2]-1
    else:
        sp[i]=3+sp[i-1]
print(len(set(sp)))
