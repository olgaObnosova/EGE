from fnmatch import fnmatch

a = open("5646.txt").readline()

k = []
def sumNechet(n):
    nach = 1
    for i in str(n[2:-2]):
        if int(i) % 2 == 1:
            nach *= int(i)
    return nach
for i in range(0, len(a) - 15):
    if fnmatch(str(a[i:i+15]), "KK43??78???34KK"):
        k.append(str(a[i:i+15]))
print(sumNechet(max(k)))

