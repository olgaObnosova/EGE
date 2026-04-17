def f(s,m):
    if s > 25: # выигр куча
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s + 2, m - 1), f(s * 2, m - 1)] # свои ходы
    return any(h) if (m -1) % 2 == 0 else all(h)


print(19, [s for s in range(1, 25) if f(s, 2)])
print(20, [s for s in range(1, 25) if not f(s, 1) and f(s,3)])
print(21, [s for s in range(1, 25) if not f(s, 2) and f(s,4)])