import sys as s
s.setrecursionlimit(1_000_000)
def f(n):
    if n<=10:
        return n
    return n-7+f(n-21)
print((f(185_734)-f(185_650))/f(40))
# sp =[0]*186_900
# for i in range(-1000, 185_800):
#     if i <=10:
#         sp[i]=i
#     else:
#         sp[i]=i-7+sp[i-21]
# print((sp[185_734]-sp[185_650])/sp[40])