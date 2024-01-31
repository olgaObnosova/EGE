def delit(n):
    s=set()
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return list(s)
for i in range(224466,664423):
    if i%5==0 and i%7==0 and i%13==0 and\
       i%25!=0 and i%49!=0 and i%169!=0:
        f=delit(i)
        f.sort()
        if f[-1]<=100000 and f[-1]%100==19:
            print(i)
            print(max(f))
    
    
