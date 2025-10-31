maxx=0
for i in range(1000):
    n=bin(i)[2:]
    if i%5==0:
        n = '1' +n+ n[-2:]
    else:
        r =bin(i%5)[2:]
        n = r+n
    r=int(n, 2)
    if r>=maxx and r<=223:
        maxx=r
print(maxx)