def f(s, h, ph):
    if s >= 82:
        return h % 2 == ph % 2
    if h == ph:
        return False
    combinations = [f(s + 2, h + 1, ph), f(s + 4, h + 1, ph),
                    f(s * 3, h + 1, ph)]
    return any(combinations) if h % 2 != ph % 2 else all(combinations)


for s in range(1, 82):
    for ph in range(1, 5):
        if f(s, 0, ph):
            if ph == 4:
                print(s)
            break


#19: 10
#20: 922
#21: 21
