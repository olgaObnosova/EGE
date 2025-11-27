from re import *
with open('24_7600.txt') as f:
    f=f.readline()
reg = r'(?:[^QRS]|Q(?![QRS])|R(?![QRS])|S(?![QRS]))+[QRS]?'
sp=findall(reg, f)
st=max(sp, key=len) #R
print(st[-10:])
ind = f.index(st)
print(ind)
print(f[876977+544-10:876977+544+10])