f = [0] * 10_004

for n in range(10_003, 0, -1):
    if n >= 10000:
        f[n] = 1
    if n < 10000 and n % 2 == 0:
        f[n] = f[n+3] + 7
    if n < 10000 and n % 2 != 0:
        f[n] = f[n+1] - 3
print(f[50]-f[57])