sp=[0]*41
sp[1]=1
for i in range(2,41):
    if i%2==0 and '3' not in str(i):
        sp[i]=sp[i//2]+sp[i-1]
    elif '3' not in str(i):
        sp[i]=sp[i-1]
print(sp)
        
