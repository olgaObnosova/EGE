import fnmatch as f
def dl(n):
    s=set()
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return s
for i in range(202, 10**7):
    if str(i)==str(i)[::-1] and i%53==0:
        if f.fnmatch(str(i), '*2?2*'):
            d=dl(i)
            if len(d)>30:
                print(i, sum(d))