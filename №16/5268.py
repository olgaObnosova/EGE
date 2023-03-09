def summ(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s


sp = [0] * 101
sp[1] = 1
sp[2] = 1
for i in range(3, 101):
    if summ(i) % 2 == 0:
        sp[i] = sp[i - 1] - sp[i - 2]
    else:
        sp[i] = sp[i - 1] + sp[i // 2]
print(sp)
