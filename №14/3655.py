def per(a, n):
    k = 0
    while a > 0:
        if (a % n)%2 != 0:
            k += 1
        a = a // n
    return k

s=0
for i in range(2, 11):
    if not (per(3456, i)):
        s+=i
        print(i)
print(s)