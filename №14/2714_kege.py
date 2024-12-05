def f(st, e, k):
    if st>e:
        return 0
    elif st==e and k==6:
        return 1
    return f(st+1, e, k+abs(st%2-1))+\
        f(st+3, e, k+abs(st%2-1))+f(st+5, e, k+abs(st%2-1))

print(f(3, 25, 0))