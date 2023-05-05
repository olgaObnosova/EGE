import math


def prostDelitel(n):
    for q in range(1, int(n**0.5)+1):
        if n % q ==0 and q != 1 and q != n:
            return False
    return True


for i in range(2, 15):
    g = math.factorial(i)
    c = []
    for j in range(2, i + 1):
        if prostDelitel(j):
            c.append(j)
    if len(c) % 2 != 0:
        print(i, len(c))