k = 0
for a in range(1,3000):
    f=1
    for x in range(1,2000):

        f*= ((a%5==0)and((2020%a!=0)\
             <=((x%1718==0)<=(2023%a==0))))

    if f:
        print(a)
