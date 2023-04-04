def f(n):
    if n==0:
        return 0
    elif n%2==1:
        return f(n-1)+1
    elif n%2==0:
        return f(n//2)
for i in range(100):
    print(f(i), i, bin(i))