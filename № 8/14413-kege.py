import itertools as t
s=set()
comb = list(t.permutations('СОРТИРОВКА', r=10))
for x in comb:
    x = ''.join(x)
    y = x
    y = y.replace('С','*')
    y = y.replace('Р', '*')
    y = y.replace('Т', '*')
    y = y.replace('В', '*')
    y = y.replace('К', '*')
    y = y.replace('А', '@')
    y = y.replace('О', '@')
    y = y.replace('И', '@')
    if '***' not in y and '@@@' not in y:
        s.add(x)
print(len(s))
