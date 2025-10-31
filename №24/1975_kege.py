with open('24_1975.txt') as f:
    f=f.readline().split('PP')
maxx = 0
for x in f:
    if len(x)>maxx:
        maxx=max(maxx, len(x))
        otv = x
print(maxx+2)
print(otv)
