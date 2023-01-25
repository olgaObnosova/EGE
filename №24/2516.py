file = open('24-2.txt')
data = file.read()
count = 0
maxc = 0
for i in data:
    if i in 'ACD':
        count += 1
        continue
    if maxc < count:
        maxc = count
    count = 0
print('', maxc)
