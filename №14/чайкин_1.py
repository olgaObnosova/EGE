x = 5 * 3 ** 1917 + 6 * 2 ** 1878 + 7 * 3 ** 1870 - 1991
s = ""
while x != 0:
    s += str(x % 17)
    x //= 17
s = s[::-1]
#print(s)
maxx = 0
maxx_index = 0
for i in range(17):
    if maxx < s.count(str(i)):
        maxx = s.count(str(i))
        maxx_index = i
print(maxx_index, maxx)