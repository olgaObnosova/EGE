sp=[0]*12
sp[0]=0
sp[1]=1
l=0
for i in range(2,len(sp)):
    if l<2:
        sp[i]+=sp[i-1]
        sp[i]+=sp[i-2]
        if i%2==0:
            l+=1
            sp[i]+=sp[i//2]
    else:
        sp[i]+=sp[i-1]
        sp[i]+=sp[i-2]
        #l-=1
print(sp)
