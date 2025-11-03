with open('24_7600.txt') as f:
    f=f.readline()
f=f.replace('Q', '*')
f=f.replace('R', '*')
f=f.replace('S', '*')
f=f.split('**')
maxx=0
for x in f:
    maxx=max(maxx, len(x))
print(maxx) #544