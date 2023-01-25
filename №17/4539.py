with open ('17⁄4539.txt') as f:
    c = m = 0
    l = [int(i) for i in f]
    for i in range(len(l) - 1):
        if (abs(l[i]) % 100 == 17 or abs(l[i + 1]) % 100 == 17) and abs(l[i] + l[i + 1]) % 2 == 0:
            c += 1
            m = max(l[i] + l[i + 1], m)
print(c)
print(m)