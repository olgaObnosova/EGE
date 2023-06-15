mx=0
for i in range(1000):
    n=bin(i)[2:]
    if i%5==0:
        n='1'+n+n[-2:]
    else:
        ost=bin(i%5)[2:]
    r=int(n,2)
    if r<223:
        mx=max(mx,r)
print(mx)