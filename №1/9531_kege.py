from itertools import *

s = '345 35 128 156 124 478 68 367'.split()
v = 'АБ БД ДЕ ЕЖ ЖЗ ЗА ЗЕ АВ ВБ ВГ ГД'.split()

print(*range(1, 9))
for p in permutations('АБВГДЕЖЗ'):
    if all(str(p.index(b) + 1) in s[p.index(a)] for a, b in v):
        print(*p)