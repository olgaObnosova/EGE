with open('4710.txt') as f:
    f = f.readline()
f = f.replace('A', '*')
f = f.replace('O', '*')
f = f.replace('C', '@')
f = f.replace('D', '@')
f = f.replace('F', '@')
f = f.replace('@*', '%')
k = maxx = 0
for x in f:
    if x == '%':
        k += 1
        maxx = max(maxx, k)
    else:
        #maxx = max(maxx, k)
        k = 0

print(maxx)