def delit(n):
    s=set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return list(s)
count=0
for i in range(200000001,2000000000):
    r=delit(i)
    
    if len(r)>=5:
        r=sorted(r)
        pr=r[0]*r[1]*r[2]*r[3]*r[4]
        if 0<pr<i:
            
            print(i, pr)
            count+=1
            if count==5:
                break
        
