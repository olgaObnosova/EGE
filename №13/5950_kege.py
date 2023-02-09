strok = 'АБДЕ БВЗ ВЖЗ ГАБ ДЕИ ЕЗИ ЖЛ ЗГЖЛК ИЗ КИ ЛК'
d = {x[0]: x[1:] for x in strok.split()}


print(d)
def f(s, end):
    if len(s) > 1 and s[-1] == end:
        print(s)
        return 1
    elif s[-1] in s[:-1]:
        return 0
    return sum(f(s+c, end) for c in d[s[-1]])
print(f('И','И'))