from itertools import product

def f(command):
    ch = 155
    for i in command:
        if i == "1":
            ch += 5
        else:
            ch*= 2
    return ch

zn = set()
algs = product("12", repeat=15)
for posl in algs:
    zn.add(f(posl))
print(len(zn))