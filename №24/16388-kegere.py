from re import *
with open('24_16388.txt') as f:
    f=f.readline()
reg = r'(?:KLMN)+' # без учета неполности
sp = findall(reg, f)
str = max(sp, key = len)
print(len(str))