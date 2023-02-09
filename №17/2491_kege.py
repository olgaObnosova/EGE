k = 0
maxx = 0
with open('2491.txt') as f:
    sp = [int(x) for x in f]
sr = sum(sp) / len(sp)
for i in range(len(sp) - 2):
    if (sp[i] < sr or sp[i + 1] < sr or sp[i + 2] < sr) and \
            '9' in str(sp[i]) and '9' in str(sp[i + 1]) and\
            '9' in str(sp[i + 2]):
        k += 1
        maxx = max(maxx, sp[i] + sp[i + 1] + sp[i + 2])
print(k)
print(maxx)
