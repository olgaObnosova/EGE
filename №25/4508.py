n = 97**3
k = 0
while k != 5:
    d = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d.append(i)
            if i != n // i:
                d.append(n // i)
    d.sort()

    k3 = 0
    mn = 0
    for j in d:
        if len(str(j)) == 3 and j % 10 == 3:
            k3 += 1
            if mn == 0:
                mn = j
    if k3 == 3:
        print(n, mn)
        k += 1

    n += 1
