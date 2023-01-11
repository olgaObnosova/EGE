def delit(n):
    s=set()
    for i in range(2,int(n**0.5)):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return list(s)
count=0
for i in range(10_000_000,100_000_000):
    f=delit(i)
    f.sort()
    if len(f)>=2 and (f[-1]+f[-2])<10_000:
        count+=1
        print(f[-1]+f[-2])
    if count==6:
        break
