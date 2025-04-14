def delit(n):
    s=set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:

            s.add(n//i)
            s.add(i)
            
    if len(s)<3:
        return 0
    return list(s)
for i in range(10_000_001,20_000_001):
    f=delit(i)
    #print(f)
    if f:
        f.sort()
        #print(f)
        summ=f[-1]+f[-2]+f[-3]        
        summ=list(str(summ))
        summ = [int(x) for x in summ]
        summ2=summ.copy()
        summ.sort()               
        if summ==summ2:
            print(summ)
