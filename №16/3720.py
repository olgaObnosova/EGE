def f(n):
    if n < 2:
        return n
    elif n % 2 == 0:
        return f(n / 2) + 1
    else:
        return f(3 * n + 1) + 1

c = []
for i in range(1, 101):
    m = int(f(i))
    if m > 100:
        c.append(m)
print(len(c))