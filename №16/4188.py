sp = [0] * 110
sp[0] = 1
for i in range(1, 109):
    if 0 < i <= 10:
        sp[i] = sp[i - 1]
    if 10 < i < 100:
        sp[i] = sp[i - 3] * 2.2
    if i >= 100:
        sp[i] = sp[i - 2] * 1.7

print(sp[40])
