for i in range(128):
    n=bin(i)[2:]
    n=(8-len(n))*'0'+n
    n=n.replace('0','*')
    n = n.replace('1', '0')
    n = n.replace('*', '1')
    n=int(n, 2)+1
    if n==153:
        print(i)
