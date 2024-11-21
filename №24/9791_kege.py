import re as r
with open('9791.txt') as f:
    f=f.readline()
maxx=0
sp=r.findall(r'[0123456789ABCDEF]+', f)
for x in sp:
    maxx=max(maxx, len(x))
print(maxx)
