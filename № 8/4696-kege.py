# def vosm(t):
#     r = ''
#     while t != 0:
#         r += str(t%8)
#         t //= 8
#     return r[::-1]
# k = 0
# for x in range(1000, 100000):
#     x = vosm(x) #10000 oct(x)
#     if len(x)==5 and x.count('6') == 1 \
#             and '16' not in x and '36' not in x \
#             and '56' not in x and '76' not in x \
#             and '61' not in x and '63' not in x \
#             and '65' not in x and '67' not in x:
#         k += 1
# print(k)
import itertools as t
comb =list(t.product('01234567', repeat = 5))
k=0
for x in comb:
    x=''.join(x)
    if x[0]!='0' and  x.count('6') == 1 \
            and '16' not in x and '36' not in x \
            and '56' not in x and '76' not in x \
            and '61' not in x and '63' not in x \
             and '65' not in x and '67' not in x:
        k+=1
print(k)