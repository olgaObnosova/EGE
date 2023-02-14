def F(n):
    if n == 0:
        return 3
    if n > 0 and n <= 15:
        return  F(n-1)
    if n > 15 and n < 100:
        return 2.5*F(n-3)
    if n >= 100:
        return 3.3*F(n-2)
print(F(100))