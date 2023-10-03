def f(a, h, ph, SUPER):
    if a >= 20:
        return h % 2 == ph % 2
    elif h == ph:
        return False
    if SUPER:
        comb = [f(a * 2, h + 1, ph, True), f(a + 2, h + 1, ph, True)]
    else:
        comb = [f(a * 2, h + 1, ph, False), f(a + 2, h + 1, ph, False), f(a, h + 1, ph, True)]

    return any(comb) if (h + 1) % 2 == ph % 2 else all(comb)

for a in range(1, 20):
    for ph in range(100):
        if f(a, 0, ph, False):
            if ph == 4:
                print(a)
            break

# 19 - 5
# 20 - 8 9
# 21 - 1 7