def f(n):
    if n==0:
        return 1
    if 0<n<=10:
        return f(n-1)
    if 10<n<100:
        return f(n-3)*2.2
    if n>100:
        return f(n-2)*1.7
print(f(40))
