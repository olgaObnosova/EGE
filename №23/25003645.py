#https://kompege.ru/variant?kim=25003645
def f(start,stop):
    if start>stop:
        return 0
    elif start==stop:
        return 1
    else:
        return f(start+1,stop)+f(start+2,stop)
print(f(11,17)*f(17,29))
print(f(11,23)*f(23,29))
print(f(11,17)*f(17,23)*f(23,29))
print(f(11,17)*f(17,29)+f(11,23)*f(23,29)-f(11,17)*f(17,23)*f(23,29))
