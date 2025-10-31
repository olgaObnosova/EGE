with open('24_1302.txt') as f:
    f=f.readline()
f=f.replace('XZZY', '*')
f=f.split('*')
maxx=0
for x in f:
    maxx=max(maxx, len(x))
print(maxx) # надо смотреть начало и конец