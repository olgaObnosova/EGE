with open('5400.txt') as f:
    f = f.readline()
f = f.replace('2', '*')
f = f.replace('3', '*')
f = f.replace('4', '*')
f = f.replace('5', '*')
f = f.replace('6', '*')
f = f.replace('7', '*')
f = f.replace('8', '*')
f = f.replace('9', '*')
f = f.split('*')
maxx = 0
for x in f:
    if len(x) >= 2 and x[0] == '0' and x[-1] == '1':
        if len(x) > maxx:
            maxx = len(x)
            b = x
print(b, maxx)
