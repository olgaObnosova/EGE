def f(n):
    if n <= 1:
        return n
    elif n > 1 and n%3==0:
        return n+f(n/3)
    elif n > 3 and n%3!=0:
        return n+f(n+3)
print(f(81))
# я не смог сделать проверку на тип данных, поэтому получается только подбором.
# числа до 81 не выводятся

