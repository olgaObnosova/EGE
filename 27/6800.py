with open('27_6800a.txt') as f:
    n, k = map(int, f.readline().split())
    sp=[int(x) for x in f]
maxx=0
for i in range(len(sp)):
    s=0
    for j in range(i, len(sp)):
        s+=sp[j]
        if j-i>=k:
            maxx=max(maxx,s)
print(maxx)