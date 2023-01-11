f=open('12.txt')
sp=[]
for line in f:
    sp.append(int(line))
k=0
minn=999999999999999
for i in range(len(sp)-1):
    if sp[i]%5==0 or sp[i+1]%5==0:
        k+=1
        minn=min(minn,sp[i]+sp[i+1])
print(k)
print(minn)
        
    
