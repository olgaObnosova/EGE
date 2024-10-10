for i in range(100):
    n=bin(i)[2:]
    if i%2==0:
        n=n+'0'
    else:
        n=n+'1'
    if n.count('1')%2==0:
        n=n+n[-2]*2
    else:
        n = n + n[-1] * 2
    r=int(n, 2)
    if r>50:
        print(i, n, r)