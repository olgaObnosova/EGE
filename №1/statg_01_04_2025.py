import  itertools as t
buk = 'GD GE ED DF EC FA CA CB AB'.split()
cif = '45 347 27 125 146 57 236'.split()
print('1 2 3 4 5 6 7')
for x in t.permutations('ABCDEFG'):
    if all(str(x.index(b)+1)  in cif[x.index(a)] for a, b in buk):
        print(*x)