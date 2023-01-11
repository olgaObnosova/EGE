n, m = map(int, input().split())
n = int('1' * n)
m = int('1' * m)
while m != 0 and n != 0:
    if n > m:
        n = n % m
    else:
        m = m % n
print(max(m, n))
