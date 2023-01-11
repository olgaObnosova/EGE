def f(n):
    if n==8 or n<=2:
        return 0
    if n==3:
        return 1
    if n>3 and n!=8:
        return f(n-2)+f(n-1)
    
for i in range(100):
    if f(i)==25:
        print(i)
