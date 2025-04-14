import itertools as t
gl = 'иаэ'
sogl = 'дгш'
k=0
comb = list(t.product('дгиашэ', repeat = 5))
for x in comb:
    x=''.join(x)
    if x[0] not in gl and x[-1] not in sogl:
        k+=1
print(k)
