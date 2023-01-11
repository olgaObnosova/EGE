f=open('25006980.txt')
sp=[]
count=0
maxs=-10001
for line in f:
    sp.append(int(line))
for i in range(len(sp)-1):
    if abs(sp[i]+sp[i+1])%3==0 \
       and abs(sp[i]+sp[i+1])%6!=0 \
       and abs(sp[i]*sp[i+1])%10==8:
        count+=1
        maxs=max(maxs,sp[i]+sp[i+1])
    
print(count, maxs)  
print(-23//10)
