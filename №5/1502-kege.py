for n in range(1, 1000):
    r = n - n%4
    r = bin(r)[2:] #100111
    sm = r.count('1') % 2
    r = r + str(sm)
    sm = r.count('1') % 2
    r = r + str(sm)
    r =int(r, 2)
    if r<64:
        print(n)
