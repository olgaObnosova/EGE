#https://kompege.ru/variant?kim=25005475
for a in range(100):
    f=1
    for x in range(1000):
        for y in range(1000):
            f*=(2*y+x!=70 or x<y or a<x)
    if f:
        print(a)
