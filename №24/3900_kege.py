with open('3900.txt') as f:
    f = f.readline().split('A')
sp = [f[0]]
maxx=0
for x in f[1:]:
    if x == sp[-1] and x!='':
        sp.append(x)
        maxx = max(maxx,len('A'.join(sp)))
    else:
        sp = [x]
print(maxx+2)
