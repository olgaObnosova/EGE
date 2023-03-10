with open('4605_a.txt') as f:
    n = f.readline()
    sp = []
    s = 0
    otv = 0
    for line in f:
        a = int(line.split()[0])
        b = int(line.split()[1])
        sp.append((a, b // 36 + bool(b % 36)))
        s += b // 36 + bool(b % 36)
minn = float('inf')
for i in range(len(sp)):
    otv+=abs(sp[0][0]-sp[i][0])*sp[i][1]
prs = 0
#print(otv)
levs = sp[0][1]
for i in range(1, len(sp)):
    prs = s - levs
    rast = abs(sp[i][0]-sp[i-1][0])
    otv = otv - prs * rast + levs*rast
    levs+=sp[i][1]
    minn = min(minn, otv)
print(minn)