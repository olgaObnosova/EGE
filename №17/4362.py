s = 0
maxx = 0
with open('3z.txt') as f:
    a = []
    for line in f:
        a.append(int(line))
for i in range(len(a)-2):
    n1 = a[i]
    n2 = a[i + 1]
    n3 = a[i + 2]
    cnt = 0
    for x in (bin(n1)[2:], bin(n2)[2:], bin(n3)[2:]):
        if x.count('1') >= 3 and x.count('0') >= 1:
            cnt += 1
    if cnt >= 2:
        s += 1
    maxx = max(maxx, n1, n2, n3)
print(s, maxx)
