def sm(n):
    s = 0
    while n != 0:
        s += n % 10
        n = n // 10
    return s


def f(s, e, s2, ssm):
    if s > e:
        return 0
    elif s == e and (s2==7 and ssm==7):
        #print(ssm, s2)
        return 1
    return f(s + 2, e, s2 + 1, ssm)\
        + f(s + sm(s), e, s2, ssm+1)


print(f(1, 70, 0, 0))
