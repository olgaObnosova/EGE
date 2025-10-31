with open('24_17878.txt') as f:
    f = f.readline()
k = 0
f = f.replace('--', '@')
f = f.replace('-*', '@')
f = f.replace('*-', '@')
f = f.replace('**', '@')
f = f.split('@')
print(f[:5])
maxl = 0
for x in f:
    # print(x)
    try:
        if len(x) > 0 and eval(x):
            if maxl < len(x):
                maxl = max(maxl, len(x))
                otv = x
    except:
        continue
print(maxl)
print(otv)
