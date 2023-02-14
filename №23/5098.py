sp=[0]*47
sp[3]=1
for i in range(4, 47):
    sp[i]+=sp[i-2]
    sp[i]+=sp[i-2]
    if i%2!=0:
