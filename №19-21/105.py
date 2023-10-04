def f(a, b, h, ph):
    if  a + b >= 259:
        return h % 2 == ph % 2
    elif h == ph:
        return False
    comb = [f(a + 1, b, h + 1, ph), f(a * 2, b, h + 1, ph), f(a, b + 1, h + 1, ph),
            f(a, b * 2, h + 1, ph)]
    return any(comb) if (h + 1) % 2 == ph % 2 else all(comb)


for b in range(242):
    for ph in range(5):
        if f(17, b, 0, ph):
            if ph == 4:
                print(b)
            break

# 19) 61
# 20) 112120
# 21) 111