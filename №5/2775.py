s = set()
for i in range(20, 601):
    n = bin(i)[2:-2]
    s.add(int(n, 2))
print(len(s))
