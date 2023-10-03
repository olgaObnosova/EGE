with open('2668a.txt') as f:
    n = int(f.readline())
    sp=[int(x) for x in f]
minn=float('inf')
for i in range(len(sp)-5):
    for j in range(i+5, len(sp)):
        minn= min(minn,sp[i]**2+sp[j]**2)
print(minn)