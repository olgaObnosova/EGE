'''def f(n):
    if n <= 3:
        return n - 1
    elif n % 2 == 0:
        return f(n - 2) + n // 2 - f(n - 4)
    else:
        return f(n - 1) * n + f(n - 2)


print(f(4952) + 2 * f(4958) + f(4964))
'''
sp=[0]*5000
for i in range(len(sp)):
    if i <=3:
        sp[i] = i-1
    elif i % 2 == 0:
        sp[i]= sp[i - 2] + i // 2 - sp[i - 4]
    else:
        sp[i]=sp[i-1]*i+sp[i-2]
print(sp[4952]+2*sp[4958]+sp[4964])