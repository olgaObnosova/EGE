def dl(n):
    s=set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            if  i%100==11 and i!=11:
                s.add(i)
            if n//i%100==11 and n//i!=11:
                s.add(n//i)
    return s
k=0
for x in range(1_350_051, 10**10):
    d = dl(x)
    if len(d)>0:
        k+=1
        print(x, min(d), d)
        if k==5:
            break