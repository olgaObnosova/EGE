c = [0] * 10001

for i in range(1, 10000):
    if i ** 0.5 == int(i ** 0.5):
        c[i] = int(i ** 0.5)
for i in range(9999, 1, -1):
    if c[i] == 0:
        c[i] = c[i + 1] + 1
print(c)

print(c[4850] + c[5000])