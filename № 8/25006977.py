from itertools import *
s = list(product('ПЛЮСЁНОК',repeat = 7))
not_in = 'ПЛСНК'
gl = 'ЮЁО'
not_comb=['ЁП','ПЁ','ЛЁ','ЁЛ','СЁ','ЁС','НЁ','ЁН','КЁ','ЁК']
count = 0
for i in s:
    x = ''.join(i)
    if x[0] not in not_in:
        f=1
        for j in not_comb:
            if j in x:
                f=0
       
        if f:
            count += 1
print(count) 
