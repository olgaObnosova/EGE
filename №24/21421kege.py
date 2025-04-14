import re
with open('24_21421.txt') as f:
    f=f.readline()
reg = r'?:([1-9]|[ab])([1-9]|[ab]*)'
res = sorted(re.findall(reg, f), key=len, reverse=True)
k=0
for c in res:
    print(len(c), c)
    k+=1
    if k==5:
        break

