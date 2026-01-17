def f(x):
    if str(x).count("1")==0:
        for y in range(13):
            if (x - 3 ** y) % 103 == 0 and (x - 3 ** y) % 2 == 1:
                return (x, y)
    return 0
for i in range(200_000, 10**6):
    if f(i):
        print(f(i))