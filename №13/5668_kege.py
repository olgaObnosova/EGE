s = 'АВБ БВГ ВГД ГДВ ДА'
d = {x[0]: x[1:] for x in s.split()}


print(d)
def f(s, end):
    if len(s) > 1 and s[-1] == end:
        print(s)
        return 1
    return sum(f(s+c, end) for c in d[s[-1]])
print(f('Г','Г'))