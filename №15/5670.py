b = range(70, 81)
k = 0
for a in range(1, 100):
    f = 0
    for x in range(1, 1000):
        f += ((x % 12 == 0) and (x in b) and (x % a != 0))
    if f == 0:
        k += 1
print(k)
