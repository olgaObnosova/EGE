
def pr(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def dt(n):
    maxx=0
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            if pr(i):
                maxx=max(maxx, i)
            if pr(n//i):
                maxx=max(maxx, n//i)
    return maxx
k=0
for i in range(1_750_000, 10_750_000):
    m=dt(i)
    if m <= 15_000 and m%10==7:
        print(i)
        k+=1
    if k==5:
        break