a=5*343**8+4*49**12+7**14-98
count=0
sp=[0]*7
while a>0:
    sp[a%7]+=1
    a=a//7
print(sp)
