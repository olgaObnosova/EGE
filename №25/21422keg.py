def d(n):
    s={10**10}
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            if i!=7 and i%10==7:
                s.add(i)
            if n//i!=7 and (n//i)%10==7:
                s.add(n//i)
    return s
k=0
for i in range(1_125_000, 10_125_000):
    if min(d(i))!=10**10:
        k+=1
        print(i, min(d(i)))
        if k==5:
            break

