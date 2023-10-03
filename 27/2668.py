with open('2668b.txt') as f:
    n = int(f.readline())
    sp=[int(x) for x in f]
minpr=float('inf')
min1=float('inf')
for i in range(len(sp)-5):
    min1=min(min1, sp[i])
    minpr=min(minpr, min1**2+sp[i+5]**2)
print(minpr)