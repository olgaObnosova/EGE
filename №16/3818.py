def f(n):  
    if n < 2:  
        return 1  
    if n >= 2 and n % 2 == 0:  
        return f(n // 2) + 1  
    if n > 2 and n % 2 != 0:  
        return f(n - 3) + 3   
for i in range(1, 1000):  
    if f(i) == 31:  
        print(i)  
        break
