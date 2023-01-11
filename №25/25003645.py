#https://kompege.ru/variant?kim=25003645
def delit(n):
    d=set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            d.add(i)
            d.add(n//i)
        
    return list(d)
def prost(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
for i in range(100000000,1000000000):
    f=delit(i)
    k=0
    sp=[]
    for x in f:
        if prost(x):
            sp.append(x)
            k+=1
    if k==2 and abs(sp[0]-sp[1])==14:
        print(i)
            
    
