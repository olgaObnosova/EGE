def is_prost(N):
    for d in range(2, int(N**0.5)+1):
        if N % d == 0:
            return 0
    return 1


for P in range(99999+1):
    if is_prost(P):
        ln = len(str(P))
        for n in range(5-ln+1):
            N = int('3' + '0'*n + str(P) + '1')
            if N % 9797 == 0:
                print(N, N//9797)
    
