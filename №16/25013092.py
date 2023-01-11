def f(n):
    if n<3:
        return 1
    elif n%2==0:
        return 2*f(n-1)-f(n-2)
    else:
        return f(n-1)-2*f(n-2)-3
print(f(15))
