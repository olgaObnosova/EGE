maxx = -float("inf")
for a in range(-500, 500):
    f = 1
    for y in range(1, 200):
        for x in range(1, 200):
            f *= (x *y>a) and (a<-x)
    if f:
       maxx = max(maxx, a)
print(maxx)
