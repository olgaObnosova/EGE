def f(n):
    l = bin(n)[2:]
    if n % 2 == 0:
        return int("1" + l + "0", 2)
    else:
        return int("11" + l + "11", 2)


for n in range(1, 1000):
    if f(n) > 225:
        print(f(n))
        break


