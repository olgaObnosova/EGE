with open('3900.txt') as f:
    f = f.readline().split('A')
sp = ['!']
maxx=0
for x in f:
    if x == sp[-1] and x!='':
        sp.append(x)
        maxx = max(maxx,len('A'.join(sp)))
    else:
        sp = [x]
print(maxx+2)
