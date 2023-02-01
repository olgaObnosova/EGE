# неработает. Подумать
def f(a, h, ph):
    if a >= 65 and a <=100:
        return h % 2 == ph % 2
    elif h == ph:
        return False
    comb = [f(a + 1, h + 1, ph), f(a * 3, h + 1, ph)]
    return any(comb) if (h + 1) % 2 == ph % 2 else all(comb)


for a in range(1, 65):
    for ph in range(5):
        if f(a, 0, ph):
            if ph==4:
                print(a)
