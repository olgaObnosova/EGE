from re import *
with open('24_1205.txt') as f:
    f=f.readline()
reg = r'(?:[^GWP])+'
sp=findall(reg, f)
st=max(sp, key=len)
print(len(st))
