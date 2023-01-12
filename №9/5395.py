f = open('5395.txt')
counter = 0
for s in f:
    l = (list(map(int, s.split())))
    l.sort()
    if (l[0]**2)*2 > l[1] * l[2] and l[2] != max(l) and len(l) != len(set(l)):
        counter += 1
print(counter)
