for n in range(7, 35):
    a = int('4646', n)
    b = int('387', n+2)
    c = int('3746', n+1)
    if a+b==c:
        print(n)