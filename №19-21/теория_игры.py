from functools import lru_cache
def moves(h):
    a,b=h
    return (a+1,b),(a*2,b),(a,b+1),(a,b*2)

@lru_cache(None)
def f(h):
    if (sum(h)>=107):
        return 'end'
    if (any(f(x)=='end' for x in moves(h))):
        return 'p1'
    if (all(f(x)=='p1' for x in moves(h))):
        return 'v1'
    if (any(f(x)=='v1' for x in moves(h))):
        return 'p2'
    if (all(f(x)=='p1' or f(x)=='p2' for x in moves(h))):
        return 'v2'
    #if (any(f(x)=='p1' for x in moves(h))):
        #return '19 задача'
    
for s in range(1,94):
    h=13,s
    print(s,f(h))
    
