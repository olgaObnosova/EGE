f = open('4z.txt')
f = f.read()
f = f.replace('ZXY', '*')
f = f.replace('ZYX', '*')
s = 0
maxx = 0
for i in range(len(f)):
    if f[i] == '*':
        s += 1
        if s > maxx:
            maxx = s
    else:
        s = 0
print(maxx)
