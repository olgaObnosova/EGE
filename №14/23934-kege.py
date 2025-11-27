# for p in range(7, 37):
#     a = int('2465123', p)
#     b = int('251341', p)
#     if (a+b)%17==0:
#         print(p,(a+b)//17)
for p in range(100):
    a = 2*p**6+4*p**5+6*p**4+5*p**3+1*p**2+2*p+3
    b = 2 * p ** 5 + 5 * p ** 4 + 1 * p ** 3 + 3 * p ** 2 + 4 * p + 1
    if (a + b) % 17 == 0:
        print(p,(a+b)//17)