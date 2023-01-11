#https://kompege.ru/variant?kim=25003483
def f(start,stop):
    if start<stop:
        return 0
    elif start==stop:
        return 1
    else:
        return f(start-2,stop)+f(start-5,stop)
print(f(23,2))
