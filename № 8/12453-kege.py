import itertools as t
comb = list(t.permutations('СОВЕСТЬ', r=7))
print(len(comb))
comb1=set(comb)
print(len(comb1))
k=0
for x in comb1:
    x = ''.join(x)
    x = x.replace('С','!')
    x = x.replace('В', '!')
    x = x.replace('Т', '!')
    x = x.replace('Е', '#')
    x = x.replace('О', '#')
    x = x.replace('Ь', '#')
    if x.count('##') == 0 or x.count('!!') == 0:
        k+=1
print(k)