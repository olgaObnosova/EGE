import fnmatch as f
for i in range(3069064, 10**10):
    if i%2024==0:
        print(i)
        break
for i in range(3070408, 10**10, 2024):
    if f.fnmatch(str(i), '3?6906*4'):
        print(i)