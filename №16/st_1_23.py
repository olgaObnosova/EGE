sp=[0]*2000000000
sp[0]=0
k=0
for i in range(1,1134567005):
    sp[i]=sp[i-1]+i
for i in range(237567892, 1134567005):
    if sp[i]%3!=0:
        k+=1
print(k)
