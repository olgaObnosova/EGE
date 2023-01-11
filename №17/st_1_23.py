f=open('17_st_1_23.txt')
k=0
sp=[]
maxx=0
minn=9999999999999
for line in f:
    a=int(line)
    sp.append(a)
    if abs(a)%10==7:
        minn=min(minn,a)
for i in range(len(sp)-1):
    if (abs(sp[i])%10==7 and abs(sp[i+1])%10!=7) or\
       (abs(sp[i+1])%10==7 and abs(sp[i])%10!=7):
        if sp[i]**2+sp[i+1]**2 < minn**2:
            k+=1
            maxx=max(maxx,sp[i]**2+sp[i+1]**2)
print(k)
print(maxx)
