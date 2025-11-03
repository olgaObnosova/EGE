with open('24_9845.txt') as f:
    f=f.readline()
# f=f.replace('B', 'A')
# f=f.replace('C', 'A')
# f=f.replace('9', '8')
# f=f.replace('AA', '*')
# f=f.replace('88', '*')
# f=f.split('*')
# maxx=0
# k=0
# for x in f:
#     k+=1
#     if len(x)>maxx:
#         maxx=max(maxx, len(x))
#         otv = x
#         num =k
# print(maxx)
# print(otv)
# print(num)
# print(f[num-2:num+1])
k=1
maxx=0
for i in range(len(f)-1):
    if f[i].isdigit()!=f[i+1].isdigit():
        k+=1
        maxx=max(maxx, k)
    else:
        k=1
print(maxx)