f=open('pr.txt')
ch=f.readline()
n,k=int(ch.split()[0]),int(ch.split()[1])
sp=[30]*n
s=0
maxs=0
count=0
for line in f:
    line=int(line)
    s+=int(line)
    if line<0 and abs(line)%10==3:
        count+=1        
    if count==k:
        maxs=max(s,maxs)        
    else:
        maxs=max(maxs,s-sp[count-k])        
    sp[count]=min(sp[count],s)
    print(sp,line,s,maxs)   
print(maxs)
print(s)
