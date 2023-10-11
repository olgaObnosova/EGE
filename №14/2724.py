for x in range(5, 100):
    a = x + 3
    b = 3 * x + 1
    c = 4 * (x ** 2) + 2 * x + 3
    if a * b == c:
        print(x)
