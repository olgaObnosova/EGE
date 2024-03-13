def f(start,stop,k):
    if start>stop or k>2:
        return 0
    elif start==stop:
        return 1

    return f(start+1,stop,k)+f(start*2,stop,k+1)
print(f(1,11,0))
