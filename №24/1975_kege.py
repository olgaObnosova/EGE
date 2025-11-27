with open('24_1975.txt') as f:
    f=f.readline()
f=f.replace('PP', 'P P')
f=f.replace('PP', 'P P')
f=f.split()
maxx = 0
for x in f:
    if len(x)>maxx:
        maxx=max(maxx, len(x))
        otv = x
print(maxx)
print(otv)


