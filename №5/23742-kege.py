for n in range(1, 1000):
    r = bin(n)[2:]
    if n%3==0:
        r = r + r[-3:]
    else:
        ost = bin((n%3)*3)[2:]
        r = r + ost
    r = int(r, 2)
    #print(n, r)
    if r>=200:
        print(n)

