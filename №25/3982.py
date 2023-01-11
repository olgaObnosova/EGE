A = []
for m in range(1, 29, 2):
    for n in range(0, 11, 2):
        a = (2**m * 7**n)
        if 300_000_000 >= a >= 100_000_000:
            A.append([a, n+m])

print(sorted(A, key=lambda x: x[0]))
