def f(st, en):
    if st>en or st==16:
        return 0
    elif st==en:
        return 1
    return f(st+1, en)+f(st+3, en)+f(st**2, en)
print(f(3, 20)*f(20, 26))