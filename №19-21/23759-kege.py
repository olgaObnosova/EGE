def F(s, m):
    if s <= 30:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [F(s - 3, m - 1), F(s - 5, m - 1), F(s // 4, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print(19, [s for s in range(31, 200) if F(s, 2)])
print(20, [s for s in range(31, 200) if not F(s, 1) and F(s, 3)])
print(21, [s for s in range(31, 200) if not F(s, 2) and F(s, 4)])