with open('17.16_14653.txt') as f:
    spis = [int(line) for line in f]
maximum = 0
sp = []
for line in spis:
    if line > maximum and str(line)[-2:] == '69':
        maximum = line
    if line % 17 == 0 and line > 0:
        sp.append(line)
sp.sort()
sp = sum(sp[:2])
k = 0
minimum = 2342343423422334234783737378347
for x in range(len(spis)-3):
    perm1 = len(str(abs((spis[x])))) == 3
    perm2 = len(str(abs((spis[x+1])))) == 3
    perm3 = len(str(abs((spis[x+2])))) == 3
    perm4 = len(str(abs((spis[x+3])))) == 3
    meta1 = spis[x] % 18 == 0
    meta2 = spis[x + 1] % 18 == 0
    meta3 = spis[x + 2] % 18 == 0
    meta4 = spis[x + 3] % 18 == 0
    if (perm1 + perm2 + perm3 + perm4) == 2 and (meta1 + meta2 + meta3 + meta4) == 1 and (spis[x+3] \
+ spis[x+2] + spis[x+1] + spis[x]) % sp == 0 and (spis[x+3] * spis[x+2] * spis[x+1] * \
spis[x]) <= maximum **2:
        k += 1
        if (spis[x+3] + spis[x+2] + spis[x+1] + spis[x])**2 < minimum:
            minimum = (spis[x+3] + spis[x+2] + spis[x+1] + spis[x])**2
print(k, minimum)