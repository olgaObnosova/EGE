a = int(input())
d = 2
s = []
while d * d < a:
    if a % d == 0:
        if (a//d)**0.5 == int((a//d)**0.5):
            print(a // d)
            break
        d += 1
    else:
        d += 1

