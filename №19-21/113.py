def f(a, S, h, ph):
    if a == S:
        return h % 2 == ph % 2
    elif h == ph:
        return False
    comb = [f(min(a, S) + 1, max(a, S), h + 1, ph), f(min(a, S) + 3, max(a, S), h +1, ph)]
    return any(comb) if (h + 1) % 2 == ph % 2 else all(comb)

for S in range(1, 24):
    for ph in range(100):
        if f(13, S, 0, ph):
            if ph == 4:
                print(S)
            break

# 19 - 9
# 20 - 6 8
# 21 - 7 19