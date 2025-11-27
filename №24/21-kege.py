import re
from re import *

with open('24_21.txt') as f:
    f=f.readline()
print(f[:20])
reg =  r'(?:X(?=[^X])|Y(?=[^Y])|Z(?=[^Z]))+'
sp=findall(reg, f)
st= max(sp, key = len) #НЕ ИЩЕТ ПОСЛЕДНИЙ!!!!
# ищет только те символы, за \
# которыми не следует такой же символ, то есть \
# каждый символ из пары правильно чередуется с другим символом.
print(st)
print(f.index((st)))
print(f[81867-5: 81867+35+5])
print(len(st)+1) #YXYXYZXYXYXYZXZYXZYZYXYXYXZXYZYXYXY

