import itertools as t
sp = list(t.permutations('113', r=3))
s=set()
for x in sp:
    s.add(''.join(x))
print(s)