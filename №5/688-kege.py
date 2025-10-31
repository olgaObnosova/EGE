for i in range(256):
    t = bin(i)[2:]
    nex = 8-len(t)#00000010
    n = nex*'0'+t
    n = n[:2]+n[-2:]
    r=int(n, 2)
    if r==7:
        print(i)