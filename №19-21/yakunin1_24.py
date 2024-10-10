# s - колво камней, m - колво ходов
def f(s, m):
    if s >= 82:
        return m%2 == 0
    if m == 0:
        return False
    turns = [f(s + 2, m -1),
             f(s + 3, m - 1),
             f(s + 4, m - 1),
             f(s * 3, m - 1)]
    return any(turns) if (m-1) % 2 == 0 else all(turns)

for S in range(1, 81):
    if (not f(S, 2)) and f(S, 4):
        print(S)