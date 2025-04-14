
def f(n):
    st=set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            st.add(i)
            st.add(n//i)
    if len(st)>=3:
        return sum(sorted(st)[-3:])
    else:
        return 0
def g(n):
    if n<2:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                return False
        return True

cnt=0
for i in range(10_000_000,10**10):
    qq=f(i)
    if g(qq):
        cnt+=1
        print(i,qq)
    if cnt==5:
        break
