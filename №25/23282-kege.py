def dl(n):
    s=set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            if pr(i):
                s.add(i)
            if pr(n//i):
                s.add(n//i)
    return s
def pr(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
k=0
for i in range(5_400_001, 10**10):
    d = dl(i)
    if len(d) > 0:
        m = max(d) + min(d)
    else:
        m = 0
    if m > 60_000 and str(m)==str(m)[::-1]:
        k+=1
        print(i, m)
        if k==5:
            break