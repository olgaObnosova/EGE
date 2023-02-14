def F(n):
    if n <= 15:
        return n*n + 3*n + 9
    elif n > 15 and n % 3 == 0:
        return F(n-1) + n - 2
    else:
        return F(n-2) + n + 2
count = 0
for n in range(1,1000):
    fl = True
    for i in str(F(n)):
        if int(i) % 2 == 0:
            continue
        else:
            fl = False
            break
    if fl == True:
        count += 1
print(count)
