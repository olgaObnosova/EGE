
file = "".join(open("24_17989.txt"))
ind = file.index("JBDPDDHKJSDBWJJKHNQSSLJDSJSMLZFMPBPXKZCD")
print(file[ind-2:ind+len("JBDPDDHKJSDBWJJKHNQSSLJDSJSMLZFMPBPXKZCD") + 10])
variations = []
for x in "BCDFGHJKLMNPQRSTVWXZ":
    for y in "AEIOUY":
        variations.append(x + y)

for vari in variations:
    file = file.split(vari)
    file= "@".join(file)
file = file.split("@")
file = [i for i in file if i !=""]
file.sort(key=lambda x: len(x))
print(file[:10])
print(len(file[-1]) + 1)


