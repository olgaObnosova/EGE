sp=[0]*1402
sp[1]=1
sp[2]=1
sp[3]=1
for i in range(4,1402):
    sp[i]=sp[i-1]*(i-3)
print(sp[1401]/sp[1397])