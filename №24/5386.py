with open('5386.txt') as f:
    f = f.readline()
f = f.replace('AB', '*')
f = f.replace('OB', '*')
f = f.replace('AC', '*')
f = f.replace('OC', '*')
f = f.replace('AD', '*')
f = f.replace('OD', '*')
k = m_xx = 0
for x in f:
    if x == '*':
        k += 1
        m_xx = max(m_xx, k)
    else:
        k = 0
print(m_xx)
