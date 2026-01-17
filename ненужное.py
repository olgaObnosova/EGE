for x in range(1, 5001):
    #print(x)
    a = 7 * 13**180 + 5 * 13**120 - x
    k = 0
    while a:
        if a % 13 == 0:
            k = k + 1
        a = a // 13
    if k==60:
        print(x)