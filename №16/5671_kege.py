'''def f(n):
    if n <= 10:
        return n
    elif n >= 10_000:
        return 1
    elif n % 2 == 0:
        return n % 10 + f(n + 2)
    return f(n - 2) - (n - 1) % 10


print(f(4500) + f(5515))
'''
sp = [0] * 10_100
for i in range(11):
    sp[i] = i
for i in range(10_000, len(sp)):
    sp[i] = 1
for i in range(11, 10_000):
    if i % 2 == 0:
        sp[i] = i % 10 + sp[i + 2]
    else:
        sp[i] = sp[i - 2] - (i - 1) % 10
print(sp[4500]+sp[5515])
#print(sp)