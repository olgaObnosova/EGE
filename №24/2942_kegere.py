from re import *
with open('24_2942.txt') as f:
    f=f.readline()
reg = r'(?:AB|AC)+'
sp=findall(reg, f)
st=max(sp, key=len)
print(len(st)//2)
