import itertools
C = []
#product = list(itertools.product("ОДЕКОЛОН", repeat=3))
#print(product)
permit=list(itertools.permutations("ОДЕКОЛОН", r=8))
print(permit)
for i in product:
    if i.count('РО')==0:
        k+=1

'''
for i in product:
    if i.count("В")==1:
        current = ""
        for j in range(len(i)):
            current+=i[j]
        C.append(current)
C = sorted(C)
print(C)
for i in range(len(C)):
    if C[i].find("А")<0:
        print(i+1)
        break
'''
