def f(s, h, ph):
    if s <= 10:
        return h % 2 == ph % 2
    if h == ph:
        return False
    combinations = [f(s // 3, h + 1, ph), f(s - 10, h + 1, ph)]
    return any(combinations) if h % 2 != ph % 2 else all(combinations)


for s in range(11, 10000):
    for ph in range(1, 5):
        if f(s, 0, ph):
            if ph == 4:
                print(s)
            break


#19: 98
#20: 43128
#21: 20
