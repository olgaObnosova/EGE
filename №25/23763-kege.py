def dl(n):
    s=set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return s

def pr(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
print(dl(100))
k=0
for i in range(800_001, 10**10):
    d = dl(i)
    if len(d)>0:
        m = max(d) + min(d)
    else:
        m = 0
    if m%10 == 4:
        k+=1
        print(i, m)
        if k==5:
            break