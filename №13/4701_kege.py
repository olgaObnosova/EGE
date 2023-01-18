s = 'АБГ БД ВБАГД ГЕЖ ДЕЛИ ЕЛВ ЖЕ ИЛ КЖ ЛЖК'
d = {x[0]: x[1:] for x in s.split()}


print(d)
def f(s, end):
    if len(s) > 1 and s[-1] == end:
        return 1
    return sum(f(c+s, end) for c in d[s[-1]])
print(f('Е','Е'))