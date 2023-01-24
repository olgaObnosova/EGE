def sumn(n):
    sc = sn = 0
    n = str(n)[::-1]
    for i in range(len(n)):
        if i % 2 == 0:
            sc += int(n[i])
        else:
            sn += int(n[i])
    if sn != 0 and sc != 0 and not sn % sc:
        return True
    else:
        return False


with open('5437.txt') as f:
    sp = []
    for line in f:
        sp.append(int(line))
mins = float('inf')
k = 0
for i in range(len(sp) - 2):
    if sumn(sp[i]) and sumn(sp[i + 1]) and sumn(sp[i + 2]):
        k += 1
        mins = min(mins, sp[i] + sp[i + 1] + sp[i + 2])
print(k)
print(mins)

