maxx = 0
with open('5955.txt') as f:
    f=f.readline()
f = f.replace('A', '*')
f = f.replace('O', '*')
f = f.replace('D', '@')
f = f.replace('F', '@')
f = f.replace('C', '@')
f = f.replace('@**@', '&')
f = f.split('&')
for x in f:
    if len(x)> maxx:
        maxx=len(x)
print(maxx+6)
