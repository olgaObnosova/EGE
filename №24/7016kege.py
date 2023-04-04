with open('24_7016.txt') as f:
    f=f.readline()
maxl=0
f=f.replace('A', 'A ')# поменять вручную пробел
f=f.replace('D', ' D')
f=f.split()
for x in f:
    if (x[0]=='A' and x[-1]=='D') \
            or (x[0]=='D' and x[-1]=='A'):
        maxl=max(maxl,len(x))
print(maxl)