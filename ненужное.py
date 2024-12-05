import string as s
alf=s.digits+  s.ascii_uppercase
def f(st, e):
    if st>e or st==30 :
        return 0
    elif st==e:
        return 1
    return f(st+1, e)+f(st*2, e)+f(st*3, e)
a_60 = f(10, 30) * f(30, 70) #40
a_30 = f(10, 60) * f(60, 70) #55
print(a_30)






