def f(start, stop):
    if start>stop:
        return 0
    elif start==stop:
        return 1
    return f(start+1, stop)+f(start*2, stop)
print(f(1,10)*f(10,16))