k=0
def f(start,stop,*r):
    global k
    k+=1
    if start>stop or k>=2:
        return 0
    elif start==stop:
        return 1
    else:
        return f(start+1,stop,0)+ f(start+2,stop,0)+ f(start*2,stop, k)
print(f(1,11))
