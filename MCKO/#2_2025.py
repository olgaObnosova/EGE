for i in range(100):
    n = bin(i)[2:] # строка!!!!! 4- 100
    if i % 2==0:
        n=n+'10'
    else:
        n='1'+n+'00'
    r=int(n, 2)
    if r>107:
        print(r)
        break