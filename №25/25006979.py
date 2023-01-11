def delit(n):
    s=set()
    for i in range(2,int(n**0.5)):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return list(s)
count=0
for i in range(500001,1000000):
    d=delit(i)
    d.sort()
    for x in d:
        if x%10==8 and x!=i and x!=8:
            print(i,x)
            count+=1
            break
    if count==5:
        break
