def f(a,b):
    if a==0 and b==0:
        return 0
    elif a>b:
        return f(a-1,b)+b
    elif a<=b and b>0:
        return f(a, b-1)+a
for a in range(100,110):
    for b in range(100,110):
        print(a,b,f(a,b))
