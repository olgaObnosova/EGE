import time as t
def fn(x, a):
    return (x%128==0) <=((x%a!=0) <=(x%80!=0))
def pr(a):
    for x in range(1, 1000):
        if not(fn(x, a)):
            return False
    return True
start = t.time()
for a in range(1,1000):
    if pr(a):
        print(a)
end=t.time()
print(end-start)
