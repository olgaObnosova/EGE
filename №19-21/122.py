#122
def f(a, h, ph):
    if a == 0:
        return h % 2 == ph % 2
    elif h == ph:
        return False

    comb = []
    if a > 5:
        comb.append(f(a-5, h+1, ph))
    if a%3 != 0:
        comb.append(f(a//3, h+1, ph))
    return any(comb) if (h + 1) % 2 == ph % 2 else all(comb)


for a in range(1, 100):
    for ph in range(5):
        if f(a, 0, ph):
            if ph == 4:
                print(a)
            break
#ответ 1: 7
#ответ 2: 8 23
#ответ 3: 15 28