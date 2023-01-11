#https://kompege.ru/variant?kim=25006154
def delit(n):
    s=set()
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return list(s)
count=0
for i in range(550000,5500000):
    f=delit(i)
    #print(f)
    k=0
    maxx=0
    for x in f:
        if x%10==7:
            k+=1
            maxx=max(maxx,x)
    if k==3:
        count+=1
        print(i, maxx)
        
    if count==5:
        break
