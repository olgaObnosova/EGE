n, m = map(int, input().split())
a = list(map(int, input().split()))
i = 0
j = len(a)-1
num = 0
k = 0
while len(a) > 1:
    j = len(a) - 1
    if a[i] + a[j] <= m:
        k += 1
        a.pop(0)
        a.pop()
    else:
        a.pop()
        k += 1


print(k + len(a))
