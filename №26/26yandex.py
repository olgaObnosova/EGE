file = [[int(j) for j in i.split()] for i in open("26yx.txt").readlines()[1:]]
time = [0 for i in range(1440)]
for p in file:
    enter, exit = p
    for i in range(enter -1, exit):
        time[i] = 1

print(time.count(0))
time = "".join([str(i) for i in time])
time = [i for i in time.split("1") if i != ""]
print(len(time))
