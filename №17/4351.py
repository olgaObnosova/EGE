with open ('17⁄4351.txt') as f:
    c = m = 0
    n1 = int(f.readline())
    for s in f.readlines():
        n2 = int(s)
        if abs(n1) % 2 == 0 or abs(n2) % 2 == 0:
            c += 1
            m = max(n1 + n2, m)
            n1 = n2
print(c)
print(m)