def f(start, stop):
    if start>stop:
        return 0
    elif start == stop:
        return 1
    return f(start+1, stop) + f(int('1'+bin(start)[2:],2), stop)
print(f(1,int('11111',2)))