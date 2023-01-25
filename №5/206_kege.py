k = 0
for i in range(800, 901):
    x1 = i % 10
    x2 = i % 100 // 10
    x3 = i // 100
    maxx = max(x1, x2, x3)
    minn = min(x1, x2, x3)
    sr = (x1 + x2 + x3) - maxx - minn
    maxc = str(maxx) + str(sr)
    if minn != 0:
        minc = str(minn) + str(sr)
    elif sr != 0:
        minc = str(sr) + str(minn)
    else:
        minc = str(maxx) + str(minn)
    r = int(maxc) - int(minc)
    if r == 30:
        k += 1
print(k)
