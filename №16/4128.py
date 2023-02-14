sp=[0]*48
sp[0]=0
sp[1]=1
sp[2]=1
for i in range(3,48):
    sp[i]=sp[i-1]+sp[i-2]
print(str(sp[47])[-4:])
