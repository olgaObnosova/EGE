f=open('17_25013097.txt')
sp=[]
minn=999999999
for line in f:
    if int(line)%43==0:
        minn=min(int(line),minn)
    sp.append(int(line))
posl=minn%10
maxx=0
k=0
print(posl)
for i in range(len(sp)-1):
    if (sp[i]+sp[i+1])% minn ==0 or sp[i]%10==posl \
       or sp[i+1]%10==posl:
        k+=1
        maxx=max(maxx,sp[i],sp[i+1])
print(k)
print(maxx)
