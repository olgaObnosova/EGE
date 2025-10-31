def f(st):
    if st==8:
        return 1
    f(sum([int(x) for x in str(st)]))
print(f(44))