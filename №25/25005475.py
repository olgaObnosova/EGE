def delit(n):
    s=set()
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return list(s)
count=0
for i in range(97**3,97**4):
    f=delit(i)
    k=[]
    for j in range(len(f)):
        if len(str(f[j]))==3 and f[j]%10==3:
            k.append(f[j])                                
    if len(k)==3:
        print(i, min(k))
        count+=1
    if count==5:
        break
        
        
