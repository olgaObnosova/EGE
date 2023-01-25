with open('2.txt') as f:
    s = f.readline()
k = 0
count = 0
i = 2
while i <= len(s):
    if s[i - 2].isalpha() and not (s[i - 1].isalpha()) and s[i].isalpha():
        k += 1
        i += 3
    else:
        i += 1
        count = max(count, k)
        k = 0
count = max(k, count)
print(count)
