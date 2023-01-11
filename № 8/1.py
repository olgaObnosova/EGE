from itertools import *
# встречается не более двух гласных нет двух гласных подряд
pr = list(product('НИЧЬЯ', repeat = 3))
pr2 = list(permutations ('НИЧЬЯ', r = 3))
#print(pr)
print(pr2)
c = 0
a = 'ЯИ'
b = 'ИЯ'
d = 'ЯЯ'
r = 'ИИ'
for i in pr:
    i=''.join(i)
    #print(i)
    if (i.count('Я')+i.count('И'))==2:
        if (a not in i) and (b not in i)\
           and (d not in i) and (r not in i):
            c += 1

print(c)
