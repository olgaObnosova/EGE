def f(N):
    s = set()
    for d in range(2, int(N**0.5)+1):
        if N % d == 0:
            s.add(d)
            s.add(N//d)
        if len(s) >= 6:
            break
    if len(s) >= 3:
        return sum(sorted(s)[-3:])
    else:
        return 0


cnt = 0 # счетчик результатов
for N in range(10_000_000+1, 20_000_000):
    S = f(N)
    if S > 0:
        cc = sorted(list(str(S)))
        ss = ''.join(cc)
        if ss == str(S):
            print(N, S)
            cnt += 1
        if cnt == 5:
            break
