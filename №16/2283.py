def F(n):
    if n > 25:
        return n * n + 4 * n + 3
    if n <= 25 and n%3 == 0:
        return F(n + 1) + 2 * F(n + 4)
    else:
        return F(n + 2) + 3 * F(n + 5)
k = 0
for i in range (1, 1001):
    k += sum(map(int, str(F(i)))) == 24
print(k)