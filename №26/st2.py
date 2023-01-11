f=open('st2.txt')
sp=[]
minst=999999999999
maxfin=0
n=int(f.readline())
maxsp=[]
for line in f:
    st,fin=int(line.split()[0]),int(line.split()[1])
    maxfin=max(maxfin,fin)
    minst=min(minst,st)
    if (st>=163305600 or st==0) and (fin>163305600 or fin==0) \
       and st<604800+163305600:
        sp.append((st,fin))
sp.sort()
#print(len(sp))
count=0
maxc=0
null=[]
for i in range(len(sp)-1):
        if sp[i][1] ==0 and sp[i][0]==0:
            null.append(sp[i])

        if (sp[i][0] ==sp[i+1][0] and sp[i][0]!=0\
            and sp[i][1]!=0 and sp[i][1]==sp[i+1][1]):
            count+=1
            maxsp.append(sp[i])
        elif count>maxc:
            maxc=count
            count=0
            maxsp=[]
            
print(len(null))       
print(maxc)
#print(maxsp)
