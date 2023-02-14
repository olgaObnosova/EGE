s = 'АБ БВ ВЕЖГ ГИ ДА ЕАД ЖЕГ ИМН КДЖ ЛЖК МЖЛ НМ'
d = {x[0]: x[1:] for x in s.split()}


def f(strk, end):
    if strk[-1] == end and len(strk) > 1:
        return 1
    elif strk[-1] in strk[1:]:
        return 0
    return sum(f(strk + x, end) for x in d[strk[-1]])

print(f('Е', 'Е'))
