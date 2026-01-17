from itertools import*
k = 0
#comb = set(permutations("АМФИБРАХИЙ"))
for s in set(permutations("АМФИБРАХИЙ")):
    s="".join(s)
    if "ИИФАА" in s or "ААФИИ" in s:
        k = k + 1
print(k)