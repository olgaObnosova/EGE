k=0
def f(start,stop):
    global k
    if start%2==0:
        k+=1    
    if  start==stop:
        return 1
    elif start>stop:
        return 0
    return f(start+1,stop)+f(start+3,stop)+f(start+5,stop)
print(f(3,25))
