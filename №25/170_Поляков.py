def f(n):
    st = set()
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            st.add(i)
            st.add(n//i)
    return sorted(st)
def g(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
k = 0
for i in range(450000,10000000):
    m = [x for x in f(i) if g(x)]
    if len(m)==0:
        m=0
    else:
        m = max(m)-min(m)
    if m%29==11:
        print(i,m)
        k+=1
    if k==5:
        break