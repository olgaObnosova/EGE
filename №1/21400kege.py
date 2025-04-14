import itertools as t
buk = 'AF AD AB FD FE DC BC BG EC EG'.split()
cif = '457 567 45 136 123 247 126'.split()
print('1 2 3 4 5 6 7')
for x in t.permutations('ABCDEFG'):
    if all(str(x.index(b)+1)  in cif[x.index(a)] for a, b in buk):
        print(*x)