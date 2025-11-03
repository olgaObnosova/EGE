from re import *
with open('24_9845.txt') as f:
    f=f.readline()
reg = r'(?:[ABC][89])+(?:[ABC])?|' \
      + r'(?:[89][ABC])+(?:[89])?'
sp=findall(reg, f)
st = max(sp, key=len)
print(len(st))