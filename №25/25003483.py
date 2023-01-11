#https://kompege.ru/variant?kim=25003483
def delit(n):
    a=set()
    for i in range(2,int(n**0.5)):
        if n%i==0:
            a.add(i)
            a.add(n//i)
    if len(a)!=0:
        n=max(a)+min(a)
    else:
        n=0
            
    return n
k=0
for i in range(452022,550000):
    m=delit(i)
    if m%7==3:
        print(i,m)
        k+=1
    if k==5:
        break
    
