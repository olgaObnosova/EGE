for i in range(13):
    n = bin(i)[2:]
    if i%2==0:
        n = '10' + n #n10
    else:
        n = '1' + n + '01'
    r = int(n, 2)
    print(r)