import itertools as f

k = 0
a = list(f.permutations('МАГИСТР', r=5))
for x in a:
    if x.count('А') + x.count('И') <= 1:
        k += 1
print(k)
