with open ('17⁄4687.txt') as f:
    a = []
    c = m = 0
    l = [int(i) for i in f]
    for i in range(len(l) - 2):
        n1 = l[i]
        n2 = l[i + 1]
        n3 = l[i + 2]
        v = sum(l) // 10000
        if ((n1 <= v and n2 <= v and n3 <= v) or (n1 <= v and n2 <= v) or (n3 <= v and n2 <= v) or (n3 <= v and n1 <= v)) and (('1' in str(n1)) and ('1' in str(n2)) and ('1' in str(n3))):
            c += 1

            m = max(m, n1+n2+n3)
print(c, m)