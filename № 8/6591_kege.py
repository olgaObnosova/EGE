import itertools as t

sp = list(t.product('0123456', repeat=5))
sc = sn = k = 0
for x in sp:
    sc = sn = 0
    x = ''.join(x)
    if x[0] != '0' and x.count('6') == 1:
        for y in x:
            if int(y) % 2 == 0:
                sc += int(y)
            else:
                sn += int(y)
        if sc < sn:
            k += 1
print(k)
