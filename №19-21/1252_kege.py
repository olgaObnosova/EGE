def f(a, b, h, ph):
    if a + b >= 88:
        return h % 2 == ph % 2
    elif h == ph:
        return False
    sp = [f(a + 1, b, h + 1, ph), f(a, b + 1, h + 1, ph), \
          f(a * 3, b, h + 1, ph), f(a, b * 3, h + 1, ph)]
    return any(sp) if (h + 1) % 2 == ph % 2 else all(sp)


for b in range(1, 82):
    for ph in range(5):
        if f(6, b, 0, ph):
            if ph == 4:
                print(b)
