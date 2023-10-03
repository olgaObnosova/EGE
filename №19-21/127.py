def f(a, h, ph):
    if a >= 111:
        return h % 2 == ph % 2
    elif h == ph:
        return False
    comb = [f(a+1, h+1, ph), f(a+3, h+1, ph), f(a*4, h+1, ph)]

    return any(comb) if (h+1)%2 == ph%2 else all(comb)

for S in range(1, 110):
    for ph in range(5):
        if f(S, 0, ph):
            if ph == 4:
                print(S)
            break

# 19) 27
# 20) 24 26
# 21) 23
