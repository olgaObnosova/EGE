def factor(num):
    ans = int(num ** .5)
    s = 0
    t = 1
    while ans > 1:
        if num % ans == 0:
            t = ans
            s += ans + num // ans * (ans * ans != num)
        ans -= 1
    return s, num // t


n = 520000
cnt = 5
while cnt:
    res, max_d = factor(n)
    if res and res == int(str(res)[::-1]):
        print(n, max_d)
        cnt -= 1
    n += 1
