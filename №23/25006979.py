def f(start, stop):
    if start>stop or start==10:
        return 0
    elif start==stop:
        return 1
    else:
        return f(start+1,stop)+f(start*2, stop)+f(start**2,stop)
print(f(5,154))
