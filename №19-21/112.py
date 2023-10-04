#112
def f(a, h, ph):
    if a == 42:
        return h % 2 == ph % 2
    elif h == ph:
        return False

    comb = []
    if a > 42:
        comb.append(f(a-1, h+1, ph))
        comb.append(f(a-3, h+1, ph))
        comb.append(f(a - 7, h + 1, ph))
    if a < 42:
        comb.append(f(a+1, h+1, ph))
        comb.append(f(a + 3, h + 1, ph))
        comb.append(f(a + 7, h + 1, ph))
    return any(comb) if (h + 1) % 2 == ph % 2 else all(comb)


for a in range(1, 100):
    for ph in range(5):
        if f(a, 0, ph):
            if ph == 4:
                print(a)
            break
#ответ 1: 28
#ответ 2: 31 37
#ответ 3: 50