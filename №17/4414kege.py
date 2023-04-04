with open('4414.txt') as f:
    sp = []
    for line in f:
        sp.append(int(line))
k = 0
maxx = -999999999
for i in range(len(sp) - 1):
    for j in range(i+1, len(sp)):
        if (abs(sp[i] - sp[j])) % 36 == 0 \
                and (sp[i] % 13 == 0 or sp[j] % 13 == 0):
            k += 1
            maxx = max(maxx, sp[i] - sp[j])

print(k, maxx)
