from re import *
with open('24_6054.txt') as f:
    f=f.readline()
reg = r'(?:[BC]{2}[A])+'
sp=findall(reg, f)
st = max(sp, key=len)
print(len(st))