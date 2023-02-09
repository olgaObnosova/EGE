def delit(n):
    s = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if not prost(i):
                s.add(i)
            if not prost(n // i):
                s.add(n // i)
    return sum(s)


def prost(n):
    for j in range(2, int(n * 0.5) + 1):
        if n % j == 0:
            return False
    return True


for i in range(912671, 0, -2):
    b = delit(i)
    if b != 0 and i % b == 0:
        print(i, b)
