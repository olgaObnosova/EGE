def f(s1, s2, h, ph):
    if s1 >= 65 or s2 >= 65:
        return h % 2 == ph % 2
    if h == ph:
        return False
    if s1 > s2:
        combinations = [f(s1 + 1, s2, h + 1, ph), f(s1 + 2, s2, h + 1, ph),
                        f(s1 + 3, s2, h + 1, ph), f(s1, s2 * 2, h + 1, ph)]
    elif s2 > s1:
        combinations = [f(s1, s2 + 1, h + 1, ph), f(s1, s2 + 2, h + 1, ph),
                        f(s1, s2 + 3, h + 1, ph), f(s1 * 2, s2, h + 1, ph)]
    else:
        combinations = [f(s1 + 1, s2, h + 1, ph), f(s1 + 2, s2, h + 1, ph),
                        f(s1 + 3, s2, h + 1, ph), f(s1, s2 + 1, h + 1, ph),
                        f(s1, s2 + 2, h + 1, ph), f(s1, s2 + 3, h + 1, ph)]
    return any(combinations) if h % 2 != ph % 2 else all(combinations)


for s2 in range(1, 65):
    for ph in range(1, 5):
        if f(26, s2, 0, ph):
            if ph == 4:
                print(s2)
            break


#19: 63
#20: 3660
#21: 57
