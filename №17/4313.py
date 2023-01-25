s = 0
maxx = 0
with open('1z.txt') as f:
    a = []
    for line in f:
        a.append(int(line))
for i in range(len(a)):
    d = a[i]
    ss = 5
    res = ''
    while d > 0:
        res = str(int(d) % ss) + res
        d = d // ss
    if int(bin(a[i])[2:]) % 10000 == 1001 and int(res) % 100 == 11:
        s += a[i]
        if maxx < a[i]:
            maxx = a[i]
print(maxx, s)
