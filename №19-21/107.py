def f(a, b, c, h, ph):
    if (a + b + c) >= 73:
        return h % 2 == ph % 2
    elif h == ph:
        return False
    comb = [f(a+3, b, c, h+1, ph), f(a, b+3, c, h+1, ph), f(a, b, c+3, h+1, ph), \
            f(a+13, b, c, h+1, ph), f(a, b+13, c, h+1, ph), f(a, b, c+13, h+1, ph), \
            f(a+23, b, c, h+1, ph), f(a, b+23, c, h+1, ph), f(a, b, c+23, h+1, ph)]

    return any(comb) if (h+1)%2 == ph%2 else all(comb)

for S in range(1, 24):
    for ph in range(5):
        if f(2, S, 2*S, 0, ph):
            if ph == 4:
                print(S)
            break

# 19) 9
# 20) 8 14
# 21) 10 13
