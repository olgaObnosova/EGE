sp=[int(x) for x in input().split()]
n=int(input())
for i in range(len(sp)-1):
    if sp[i]>n and sp[i+1]<n:
        num=i+2
    elif sp[i]>n and sp[i+1]==n:
        num=i+3
    elif sp[i] == n and sp[i + 1] == n:
        num = i + 3
    elif n>=sp[0]:
        num = 1
    elif n<=sp[-1]:
        num = len(sp)+1
print(num)