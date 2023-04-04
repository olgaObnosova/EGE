def f(s):
    a=s[-1]
    if len(s)>1 and a==42:
        return 1
    if a<40 or a>49 or a in s[:-1]:
        return 0
    return f(s+[a-1]) + f(s+[a-3]) + f(s+[a+1]) + f(s+[a+3])
print(f([42]))