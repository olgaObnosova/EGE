s = 0
minr = float('inf')
with open('2683b.txt') as f:
    n = int(f.readline())
    for line in f:
        a, b = map(int, line.split())
        s += max(a, b)
        minr = min(minr, abs(a - b))
print(s, minr, s-minr)
