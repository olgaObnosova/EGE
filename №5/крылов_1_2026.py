maxx=0
for n in range(1, 1000):
    r=bin(n)[2:]
    if n%3==0:
        r+=r[-3:]
    else:
        ost=(n%3+1)*3
        r=r+bin(ost)[2:]
    r=int(r, 2)
    if r<=416:
        maxx=max(maxx, r)
print(maxx)
