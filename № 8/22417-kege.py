import itertools as s
sp = list(s.product('АБЕИЛРТФЦ', repeat=5))
simple = 0
k = 0
for x in sp:
    x = ''.join(x)
    k += 1
    if x[0] != 'И' and x[0] != 'Е' and x[0] != 'А' and k % 2 != 0 and x.count('Ц') == x.count('Ф'):
        simple += 1
print(simple)