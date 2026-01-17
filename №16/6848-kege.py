def f(n):
    if n<10:
        return n
    elif n%2==0:
        return f(n%10)+f(n//10)
    return f(10**n)+f(n%10)-2
for i in range(1000):
    print(i, f(i))
