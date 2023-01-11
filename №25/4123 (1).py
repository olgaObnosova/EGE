#4123
maxx = -1000000
count = 0
otv=0
for a in range(1, 5001):
    for b in range(a+1, 5001):
        for c in range(b+1, 5001):
            if (a <= b <= c) and (a*a + b*b) == c*c:
                count += 1
                if maxx> a+b+c:
                    maxx=a+b+c
                    otv=a**2+b**2
                
print(count, otv)
