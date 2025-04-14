for i in range(20000, 200000):
    n=bin(i)[2:]
    k0 = bin(n.count('0'))[2:]
    k1 = bin(n.count('1'))[2:]
    r = int(k1 + k0, 2)
    if r == 214:
        print(i)
print(bin(214)[2:])
print(int('10110', 2))
print(int('110', 2))
print(bin(134217759)[2:])