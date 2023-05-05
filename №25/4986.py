A = []
b = []
Grups = {}
def prostDeliteli(n):
    for j in range(1, int(n ** 0.5) + 1):
        if n % j == 0 and j != 1 and j != n:
            return False
    return True

def proizvChisel(n):
    a = 1
    for qqq in str(n):
        if qqq != "0":
            a *= int(qqq)
    return a


for i in range(10, 100000):
    if i == 1_000_000_001:
        break

    if prostDeliteli(int(str(i) + str(i)[::-1])):
        m = proizvChisel(int(str(i) + str(i)[::-1]))
        if m in Grups.keys():
            Grups[m].append(int(str(i) + str(i)[::-1]))
        else:
            Grups[m] = [int(str(i) + str(i)[::-1])]
    if prostDeliteli(int(str(i) + (str(i)[::-1])[1:])):
        b.append(int(str(i) + (str(i)[::-1])[1:]))
        m = proizvChisel(int(str(i) + (str(i)[::-1])[1:]))
        if m in Grups.keys():
            Grups[m].append(int(str(i) + (str(i)[::-1])[1:]))
        else:
            Grups[m] = [int(str(i) + (str(i)[::-1])[1:])]

maxxxx = 0
g = 0
for i in Grups.keys():
    if len(Grups[i]) > maxxxx:
        maxxxx = len(Grups[i])
        g = i
print(*((((sorted(Grups[g]))[::-1])[:5])[::-1]))