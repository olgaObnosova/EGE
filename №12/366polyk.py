sp=[]
for x in range(100):
    for y in range(100):
        for z in range(100):
            if 2*y+z==15 and 2*x+3*y+z==21:
                sp.append(x+y+z)
print(max(sp))