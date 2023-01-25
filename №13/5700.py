s = 'АБ БВ ВЖЕГ ГЕД ДЕЖК ЕЖ ЖЗН ЗКДЛ КЛ ЛМ МАНЗ НАБВЗ'
D = {x[0]: x[1:] for x in s.split()}
print(D)
def foo(str, e):
    if e == str[-1] and len(str) > 1:
        print(str)
        return 1
    elif str[-1] in str[:-1]:
        return 0
    return sum([foo(str + x, e) for x in D[str[-1]]])


print(foo("Ж", "Ж"))
