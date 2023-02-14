def f(s,e):
    if s == e:
        return 1
    elif s<10:
        return 0
    else:
        return f(s//10+s%10,e) + f((s//10)*(s%10),e)
cnt = 0
for x in range(10,100):
    if f(x,8):
        cnt+= 1
print(cnt)
