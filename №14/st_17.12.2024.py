def f(n):
    s0 = 0
    s6 = 0
    while n != 0:
        if  n % 7 ==0:
            s0+=1
        if  n % 7 ==6:
            s6+=1
        n = n // 7
    return s6 > s0

print(980486-275071)
for x in range(2_000_0000, 3_000_0000):
    a = 4 * 7 ** 24 + 6 * 7 ** 13 + 5 * 49 ** 4 + 2 * 343 ** 2 + 10 - x
    if f(a):
        print(x)
