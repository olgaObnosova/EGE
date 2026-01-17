def dl(n):
    s=set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return s
def f (x, C):
    A = range(7, 27)
    B={7, 11}
    return (x in C)<=((x in A) and (x not in B))

for y in range (1,1000):
    C = dl(y)
    if len(C)>0 and all(f(x,C)==1 for x in range(1,100000)):
          print (y)
          break