def f(x):
    return (x&57==0 or x&23!=0 or x&a!=0)
for a in range(1000):
    if all(f(x) for x in range(1000)):
        print(a)
        break