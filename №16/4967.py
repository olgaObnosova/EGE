c = []

l = 1
ll = 2
summ1 = 1
while ll < 29:
    l += ll
    print(ll + 2, l)
    ll += 1
    summ1 += l
print(summ1)


def f(n):
    if n == 0:
        return 5
    elif n % 2 == 0:
        return 1 + f(n / 2)
    else:
        return f(n // 2)
for i in range(1000000000, 1073741824):
    c.append(f(i))

print(summ1 - c.count(7))