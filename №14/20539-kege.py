def tr(n):
    s=''
    while n:
        s+=str(n%3)
        n=n//3
    return s[::-1]
for a in range(1000, 50_000):
    d = 3**10+3**7+3**3+2-a
    d=tr(d)
    if d.count('0')==d.count('1')==d.count('2'):
        print(a)
        break
