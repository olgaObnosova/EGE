def f(n):
    if n==0:
        return 0
    elif n%2==0:
        return f(n//10)+n%10
    return f(n//10)
print(5**7*3)