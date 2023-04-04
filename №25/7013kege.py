import fnmatch as f
def dell(n):
    s=set()
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return len(s)
for i in range(31650,10**9):
    if i%(31*2031)==0:
        print(i)
        break
sp=[2**i for i in range(35)]
#print(sp[-1])
for i in range(62961, 10**9, 2031*31):
    if f.fnmatch(str(i), '*31*65?') and i%31==0 \
            and i%2031==0 and dell(i) in sp:
                print(i, i//2031)
