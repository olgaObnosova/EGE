from itertools import product
a = list(product('01234567', repeat=5))
k = 0
for x in a:
    x = ''.join(x)
    if x[0]!='0' and '16' not in x and '61' not in x\
        and '36' not in x and '63' not in x and \
            '56' not in x and '65' not in x and \
            x.count('6') == 1:
        k += 1
print(k)