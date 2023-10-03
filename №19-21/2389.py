def f(a, b, h, ph):
    if a + b >= 77:
        return h % 2 == ph % 2
    elif h == ph:
        return False
    comb = [f(a + 1, b, h + 1, ph), f(a, b + 1, h + 1, ph), \
            f(a * 2, b, h + 1, ph), f(a, b * 2, h + 1, ph)]
    return any(comb) if (h + 1) % 2 == ph % 2 else all(comb)


for b in range(1, 70):
    for ph in range(5):
        if f(7, b, 0, ph):
            if ph == 4:# меняем вот здесь значение
                print(b)
            break
# если Ваня 1м ходом, то m=2
# если Петя 2м ходом, то m=3
# если Ваня 2м ходом, то m=4
