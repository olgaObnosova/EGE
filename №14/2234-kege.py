s = 3**72+6*3**50-7*3**26+2*3**15+155
mn = set()
while s != 0:
    ost = s%9
    mn.add(ost)
    s//=9
print(mn, len(mn))