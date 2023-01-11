def f(n):
    if n==0:
        return 0
    elif n%3==2:
        return f(n-1)+1
    elif n%3<2:
        return f((n-n%3)//3)
for i in range(1000):
    if f(i)==6:
        print(i)
