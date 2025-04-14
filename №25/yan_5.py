def deg(number):
    x = number**(1/3)
    x = int(round(x))
    if x**3 == number:
        return x
    else :
        return 0
def f(n):
    cnt = 0
    sp = []
    for z in range(2, int(n ** 0.5) + 1):
        if n % z == 0 and deg(z) % 2 != 0:
            sp.append(z)
        if n % z == 0 and deg(n//z) % 2 != 0 and z != (n//z):
            sp.append(n//z)
    if deg(n) % 2 != 0:
        sp.append(n)
    if len(sp) >= 4:
        return len(sp), max(sp)
    else:
        return 0, 0
k = 0
for i in range(228224, 531136):
    d, q = f(i)
    if q > 0:
        print(d, q)