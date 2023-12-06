def f(n):
    if n>=1000:
        return 1000
    elif n%2==0:
        return n*f(n+1)/2
    return n*f(n+1)
print(f(998)/f(1001))