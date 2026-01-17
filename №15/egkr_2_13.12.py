def f (A):
    for x in range(5000):
        for y in range(5000):
            if ((x*y<A) or (x<7*y) \
                or (343<x))==False:
                return False
    return True
for A in range (0,20000):
     if f(A):
          print (A)