def f(start, stop,k,c):
    if start > stop or k+c>1:
        return 0
    elif start == stop and k+c==1:
        return 1
    return f(start+1, stop, k,c)+ f(start+2, stop, k,c)+ \
        f(start *2, stop, k+1,c)+ f(start*3, stop, k, c+1)
print(f(1,11,0,0))