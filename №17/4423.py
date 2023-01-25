d = [int(x) for x in open('4423.txt')]

def f(x):
    return 0 <= x and x % 10 == 9

mxsum = 0
count = 0
for i in range(2,len(d)):
    if(not f(d[i - 2])) and f(d[i-1]) and (not f(d[i])):
        count += 1
        mxsum = max(mxsum, sum(d[i - 2: i + 1]))
print(count,mxsum)