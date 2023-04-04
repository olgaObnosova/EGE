sp = [0] * (45789 + 1)
sp[5001] = 1
f1 = f2 = f3 = 1
for i in range(5004, 45789 + 1):
    if f1:
        sp[i] += sp[i - 1]
        f1 = 0
        f2 = f3 = 1
    if i % 2 == 0 and f2:
        sp[i] += sp[i // 2]
        f2 = 0
        f1 = f3 = 1
    if f3:
        sp[i] += sp[i - 3]
        f3 = 0
        f1 = f2 = 1
print(sp[45789])
