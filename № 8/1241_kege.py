import itertools as f

a = list(f.product('РУСЛАН', repeat=5))
k = 0
for x in a:
    x = ''.join(x)
    if x.count('У') <= 1 and x.count('А') <= 1:
        k += 1
print(k)
