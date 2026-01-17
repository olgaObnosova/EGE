def pr(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def dl(n):
    s=[]
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            s.append(i)
            s.append(n//i)
    return s
k=0
for i in range(3_000_001, 3_000_0010):
    d = dl(i)
    if len(d)==2:
        if pr(d[0]) and pr(d[1]):
            p1 = '1' in str(d[0]) or '3' in str(d[0])
            p2 = '1' in str(d[1]) or '3' in str(d[1])
            if p1+p2==2:
                k+=1
                print(i, d)
        if k==5:
            break
