def tr(n):
    s=''
    while n:
        s+=str(n%3)
        n=n//3
    return s[::-1]
for n in range(1, 1000):
    r = tr(n)
    if n%3==0:
        r=r+r[-2:]
    else:
        sm = r.count('1')+2*r.count('2')
        sm=sm*3
        r =r+tr(sm)
    r =int(r, 3)
    if r>208 and r%2!=0:
        print(r)

