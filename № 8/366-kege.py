import itertools as t
comb = list(t.permutations('ОСЕНЬЮПРИЗЫВ', r = 12))
k=0
gl = 'ОЕИЮЬЫ'
sogl = 'СНПРЗВ'
for x in comb:
    fl=1
    x=''.join(x)
    p1 =  x[0] in gl and x[1] in sogl and \
        x[2] in gl and x[3] in sogl and\
        x[4] in gl and x[5] in sogl and\
        x[6] in gl and x[7] in sogl and\
        x[8] in gl and x[9] in sogl and \
        x[10] in gl and x[11] in sogl
    p2 = x[0] in sogl and x[1] in gl and \
         x[2] in sogl and x[3] in gl and \
         x[4] in sogl and x[5] in gl and \
         x[6] in sogl and x[7] in gl and \
         x[8] in sogl and x[9] in gl and \
         x[10] in sogl and x[11] in gl
    if p1+p2==1:
        k+=1
print(k)




