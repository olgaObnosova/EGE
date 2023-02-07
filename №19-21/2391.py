def f(a, b, h, ph):
    if a + b >= 83:
        return h % 2 == ph % 2
    elif h == ph:
        return False
    sp = [f(a + 1, b, h + 1, ph), f(a, b + 1, h + 1, ph), \
          f(a * 2, b, h + 1, ph), f(a, b * 2, h + 1, ph)]
    return any(sp) if (h + 1) % 2 == ph % 2 else all(sp)


for b in range(1, 74):
    for ph in range(5):
        if f(9, b, 0, ph):
            if ph == 4:
                print(b)
