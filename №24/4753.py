f = open('5z.txt')
f = f.readline()
f = f.replace('A', '*')
f = f.replace('E', '*')
f = f.replace('I', '*')
f = f.replace('O', '*')
f = f.replace('U', '*')
f = f.replace('Y', '*')
s = 0
maxx = 0
t = 0
for i in range(len(f)):
    if f[i] == '*':
        if s > maxx and t >= 6:
            maxx = s
        s = 0
        t = 0
    if f[i] == '.':
        t += 1
    if f[i] != '*':
        s += 1
print(maxx)
