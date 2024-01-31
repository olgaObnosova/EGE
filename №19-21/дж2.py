def f(a, b, h, ph, x):
    if a + b >= x:
        return h % 2 == ph % 2
    elif h == ph:
        return False
    sp = [f(a + 2, b, h + 1, ph, x), f(a, b + 2, h + 1, ph, x), \
          f(a * 2, b, h + 1, ph, x), f(a, b * 2, h + 1, ph, x)]
    return any(sp) if (h + 1) % 2 == ph % 2 else all(sp)


k=0
for x in range(17, 100):

    if f(8, 8 , 0, 4, x):
        k+=1
        print(x)
print(k)