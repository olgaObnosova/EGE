def tr(n):
    s=''
    while n!=0:
        s+=str(n%3)
        n//=3
    return s[::-1]
for x in range(100_000):
    a = 3**2000+3**10-x
    a = tr(a)
    if a.count('2')==2000:
        print(x)
        break