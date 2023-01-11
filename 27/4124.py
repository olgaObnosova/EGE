f = open('4124.txt')
n = int(f.readline())
s = 0
not_s = 0
minn = 10000000000
min2 = 10000000000
for i in range(n):
    x, y = map(int, f.readline().split())
    s += max(x, y)
    not_s += (x+y) - max(x, y)
    if abs(x-y) % 5 != 0 and abs(x-y) != 0:
        if minn > abs(x-y):
            minn=abs(x-y)
        elif min2 > abs(x-y):
            min2=abs(x-y)
print(s)
print(not_s)
print(minn)
print(min2)
if s % 5 != 0 and not_s % 3 != 0:
    print(s)
elif (s -minn)% 5 != 0 and (not_s + minn) % 3!= 0:
    print(s-minn)
else:
    print(s-min2)
