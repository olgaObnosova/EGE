# def f(n):
#     if n<=3:
#         return 1
#     return (n+3)*f(n-2)
# print(f(2028)/f(2024))
sp=[0]*2029
for i in range(1, 2029):
    if i<=3:
        sp[i]=1
    else:
        sp[i]=(i+3)*sp[i-2]
print(sp[2028]/sp[2024])