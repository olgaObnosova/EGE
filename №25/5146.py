def N(k):
    return 750_000_000 + k
def chetDeliteli(N): 
    delitels = set() 
    for i in range(1, int(N ** 0.5) + 1): 
        if N % i == 0: 
            if i % 2 == 0: 
                delitels.add(i)
            ii = N // i
            if ii % 2 == 0: 
                delitels.add(ii) 
    return len(delitels)

perem = 0 
for k in range(0, 100000000000, 2): 
    l = chetDeliteli(N(k)) 
    if l % 2 == 1:
        perem += 1
        print(k, l)
        if perem == 5:
            break
