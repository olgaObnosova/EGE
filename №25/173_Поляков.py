def pr(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1

def srp(n):
    st = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0 and pr(i):
            st.add(i)
    if len(st) > 0:
        f = sum(x for x in st) // len(st)
        return f
    return 0
k = 0
for i in range(650_000, 1_000_000):
    sr = srp(i)
    if sr % 37 == 23:
        print(i, sr)
        k += 1
        if k == 4:
            break