def sumc(a):
    s = 0
    while a > 0:
        s += a % 10
        a = a // 10
    return s


k = 0
for i in range(10**8, 10**10):
    n = bin(i)[2:]
    if sumc(i) % 2 == 0:
        n += 3 * '0'
    else:
        n += 3 * '1'
    n = int(n, 2)
    #print(i, n)
    if 123456789 <= n <= 1987654321:
        k += 1
print(k)
