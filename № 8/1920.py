import itertools as t
k=0
s=list(t.permutations('ЗДАНИЕ', r = 6))
for x in s:
    x = ''.join(x)
    x = x.replace('И','А')
    x = x.replace('Е', 'А')
    if 'АА' not in x:
        k+=1
print(k)
