def f(n):
    s=set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return list(s)
for i in range (1_200_000,1,-1):
    summ=0
    c=i
    r=f(i)
    r.sort()
    r=r[::-1]
    k=0
    for x in r:
        if x<c//i+1:
            summ+=x
            k+=1
            if k==3:
                break
    #if summ %2022==0 and summ!=c:
        #print(c,summ)
