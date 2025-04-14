def N(k):
    pon = set()
    for i in range(2, int(k**0.5)+1):
        if k % i == 0:
            if k % 2 == 0:
                pon.add(k)
            if (k // i) % 2 == 0:
                pon.add(k//i)
    return pon

sigma = 750000
lutipon = 0
for k in range(0, 100000):
    r = N(sigma + k)
    if len(r) % 2 != 0:
        lutipon += 1
        print(k, len(r))
    if lutipon == 5:
        break