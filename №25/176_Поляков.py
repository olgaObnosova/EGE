
def f(n):
    st=set()
    maxxc=0
    maxx=0
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            if i%2==0:
                maxxc=max(maxxc,i)
            else:
                maxx = max(maxx, i)
    if maxxc!=0 and maxx!=0:
        return abs(maxxc-maxx)
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
for i in range(250156,10**10):
    a=f(i)
    if g(a)==True and a%10==9:
        cnt+=1
        print(i,a)
    if cnt==5:
        break