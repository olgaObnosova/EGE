def f(x, y, m):
	if (x**2 + y**2)**0.5 > 14:
		return m % 2 != 0
	if m == 0:
		return 0
	h = [f(x * 2, y, m - 1), f(x, y + 4, m - 1), f(x, y + 3, m - 1)]
	return any(h) if (m - 1) % 2 == 0 else all(h)

print(19, [y for y in range(1, 14) if f(3, y, 2)])
print(20, [y for y in range(1, 14) if not f(3, y, 1) and f(3, y, 3)])
print(21, [y for y in range(1, 14) if not f(3, y, 2) and f(3, y, 4)])
print(257491/683)