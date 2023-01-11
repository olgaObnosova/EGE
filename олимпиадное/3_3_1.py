n, m = map(int, input().split())
a = list(map(int, input().split()))
i = j = 0
num = 0
while i < len(a) and j < len(a):
    if a[i] - a[j] <= m:
        j += 1
    else:
        num += n - j
        i += 1
print(num)



