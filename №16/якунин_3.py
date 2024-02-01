def f(n):
    if n>=1000:
        return 1000
    return 5*f(2*n)
print(f(5))