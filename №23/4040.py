rez = set()
def f(x, p):
    global rez
    if p == 12:
        rez .add(x)
    else:
        f(x + 1,p + 1)
        f(x * 2 - 3,p + 1)
f(3, 0)
print(len(rez))