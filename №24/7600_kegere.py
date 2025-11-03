from re import *
with open('24_7600.txt') as f:
    f=f.readline()
reg = r'(?:[^QRS]|Q(?![QRS])|R(?![QRS])|S(?![QRS]))+'
sp=findall(reg, f)
st=max(sp, key=len)
print(len(st))