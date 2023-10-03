def f(a, h, ph):
    if a >= 73:
        return h % 2 == ph % 2
    elif h == ph:
        return False
    comb = [f(a+3, h+1, ph), f(a+1, h+1, ph), f(a*2, h+1, ph)]

    return any(comb) if (h+1)%2 == ph%2 else all(comb)

for S in range(1, 72):
    for ph in range(5):
        if f(S, 0, ph):
            if ph == 4:
                print(S)
            break

# 19) 36
# 20) 18 33
# 21) 32 34
