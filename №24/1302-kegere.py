from re import *
with open('24_1302.txt') as f:
    f=f.readline()
reg = r'(?:(?!XZZY).)+'
sp=findall(reg, f)
st=max(sp, key=len) # не учитывает \
# начало ZZY
print(len(st))