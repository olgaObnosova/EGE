def f(a, S, h, ph):
    if a >= 50 or S >= 50:
        return h % 2 == ph % 2
    elif h == ph:
        return False

    comb = [f(a * 2, S, h + 1, ph), f(a + 3, S, h + 1, ph), f(a, S * 2, h + 1, ph), f(a, S + 3, h + 1, ph)]

    return any(comb) if (h + 1) % 2 == ph % 2 else all(comb)


for S in range(1, 28):
    for ph in range(100):
        if f(22, S, 0, ph):
            if ph == 4:
                print(S)
            break

# 19 - 22
# 20 - 11 21
# 21 - 18