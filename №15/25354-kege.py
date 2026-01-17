# for a in range(100_000):
#     f=1
#     for x in range(100_000):
#         for y in range(100_000):
#             f*=(78125!=y+4*x) or (a>x) and (a>y)
#     print(a)
#     if f:
#         print(a)
def f (A):
    for x in range(80_000):
        for y in range(80_000):
            if ((x*y<A) or (x<7*y) \
                or (343<x))==False:
                return False
    return True
for A in range (0,80_000):
     if f(A):
          print (A)