#f = open('27.txt')
#n, k = map(int, f.readline().split())
prefix = [0]*3
k=3
s, ans = 0, 0
n=[1,2,3,4,5,6,7,8,9]
for x in n:
    #x = int(f.readline())
    s += x
    if s % k == 0:
        ans += 1
    ans += prefix[s % k]
    prefix[s % k] += 1
    print(s,prefix,ans)
print(ans)
