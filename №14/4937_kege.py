for x in range(79, -1, -1):
    a = 3 * 80 ** 3 + x * 80 ** 2 + 7 * 80 + 5
    b = 80 ** 3 + 4 * 80 ** 2 + 80 * x
    if (a + b) % 17 == 0:
        print((a + b) // 17)
        break
