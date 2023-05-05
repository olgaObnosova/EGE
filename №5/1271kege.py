mn = 99999
for i in range(1, 100):
    s = 0
    n = bin(i)[2:]
    if i % 2 == 0:
        n = '1' + n + '0'
    else:
        n = '11' + n + '10'
    n = int(n, 2)
    for x in str(n):
        s += int(x)
    if s > 17 and n < mn:
        mn = n
        otv = s
print(bin(otv))
