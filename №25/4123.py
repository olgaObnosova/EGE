A = []
k = 5000 ** 2
for a in range(1, 5000):
    for b in range(a, 5000):
        c = (a*a + b*b) ** 0.5
        if int(c) == c and c <= 5000 and a <= b <= c:
            A.append([a+b+int(c), int(c)])
print(len(A), max(A, key=lambda x: x[0])[1])
