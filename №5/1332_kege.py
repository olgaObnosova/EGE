for i in range(1000):
    n=bin(i)[2:] #1_100-122-022 - 1011
    n1 = n[1:]
    n1=n1.replace('0','*')
    n1=n1.replace('1', '0')
    n1=n1.replace('*', '1')
    n=n[0]+n1
    r = int(n, 2)
    r=r+i
    if i%2!=0 and r>99:
        print(i)
