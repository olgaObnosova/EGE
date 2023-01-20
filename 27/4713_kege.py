with open('4713_B.txt') as f:
    n = int(f.readline())
    sp = []
    s = 0
    minn = 9999999999999999999999999999999999999
    for line in f:
        a, b = map(int, line.split())
        b = b // 36 + bool(b % 36)
        sp.append((a, b))
        s += b
print(s)
summ = 0
pravs = 0
levs = sp[0][1]
sp.sort()
for i in range(len(sp)):
    summ += abs(sp[0][0] - sp[i][0]) * sp[i][1]
#print(sp)
print(summ)
for i in range(1,len(sp)):
    pravs = (s - levs)
    summ = summ + (levs*abs(sp[i][0]-sp[i-1][0])- pravs*abs(sp[i][0]-sp[i-1][0]))
    #print(levs, pravs, summ, i,abs(sp[i][0]-sp[i-1][0]))
    levs += sp[i][1]
    minn = min(minn, summ)
print(minn)
