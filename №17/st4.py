f=open('17_st4.txt')
minn=100000
maxx=0
count=0
sp=[]
for i in f:
    sp.append(int(i))
    if int(i)%2==1:
        minn=min(minn,int(i))
for i in range(len(sp)-1):
    if ((sp[i]%3==0 and sp[i+1]%3!=0) \
       or (sp[i+1]%3==0 and sp[i]%3!=0))\
       and abs(sp[i]-sp[i+1])<minn:
        count+=1
        maxx=max(maxx,abs(sp[i]-sp[i+1]))
print(count, maxx)
