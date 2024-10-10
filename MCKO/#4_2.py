for i in range(100):
    n=bin(i)[2:]
    if i%2==0:
        n=n+'00'
    else:
        n=n+'11'
    if n.count('1')%2==0:
        n=n+n[-2]
    else:
        n = n + n[-1]
    r=int(n, 2)
    if r>80:
        print(i, n, r)