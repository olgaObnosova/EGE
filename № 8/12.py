import itertools as t
a=list(t.product("АКРУ", repeat=5))
#print(a[:10])
k=0
for x in a:
    k+=1
    x=''.join(x)
    if x[0]=='К':
        print(k)
