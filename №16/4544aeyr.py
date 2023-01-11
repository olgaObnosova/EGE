def f(n):
    if n==0:
        return 0
    elif n%2==0:
        return f(n//2)-1
    else:
        return 3+f(n-1)
s=set()   
for i in range(1000):
    s.add(f(i))
print(len(s))    
