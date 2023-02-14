def f(n):
    if n == 0:
        return 1
    elif n % 2 !=0:
        return 1+f(n-1)
    else:
         return f(n/2)
cnt = 0
for n in range(1,500000000):
    if f(n) == 3:
        cnt+=1
        print(cnt)
print(cnt)
