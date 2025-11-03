from re import *
with open('24_4602.txt') as f:
    f=f.readline()
reg = r'(?:[BCD][AO])+'
sp=findall(reg, f)
st = max(sp, key=len)
print(len(st)//2)