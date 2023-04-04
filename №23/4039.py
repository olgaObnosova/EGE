def f(start, k):
    if k==13:
        rez.add(start)
        return
    return f(start+3, k+1), f(start*2+1, k+1)
rez=set()
f(2,0)
print(len(rez))
