with open('4713_A.txt') as f:
    n = int(f.readline())
    sp = []
    s = 0
    minn = 9999999999999999999999999999999999999
    for line in f:
        a, b = map(int, line.split())
        b = b // 36 + bool(b % 36)
        sp.append((a, b))
sp.sort()
for i in range(len(sp)):
    s=0
    for j in range(len(sp)):
        s+=abs(sp[i][0]-sp[j][0])*sp[j][1]
    minn=min(s,minn)
print(minn)
