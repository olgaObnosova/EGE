with open('17_23952.txt') as f:
    sp = [int(x) for x in f]
max93 = max([x for x in sp if x % 100 == 93])
for x in sp:
    if x % 100 == 93:
        max93 = max(max93, x)
k = sm = 0
for i in range(len(sp) - 1):
    p1 = sp[i] > max93
    p2 = sp[i + 1] > max93
    if (p1 + p2) == 1:
        if str(sp[i])[0] == '9' \
                or str(sp[i + 1])[0] == '9':
            k += 1
            if sp[i] > max93:
                sm += sp[i]
            if sp[i+1]>max93:
                sm+=sp[i+1]
print(k, sm)

