
def f(n):
    if n<15:
        return 4
    else:
        if n%3==0:
            return f(2*n/3) + n-1
        if n%3!=0:
            return f(n-1) +3
for x in range(1000):
    if f(x)==251:
        print(x)