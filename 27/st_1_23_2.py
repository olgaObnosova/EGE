co = 0
with open('25-B.txt') as f:
    pk = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    n = f.readline()
    for i in f.readlines():
        a = int(i.strip('\n'))
        del_3 = a % 3
        step_2 = 0
        while a % 2 == 0:
            step_2 += 1
            a //= 2
        step_2 = min(step_2, 10)
        for j in range(10 - step_2, 11):
            co += pk[(3 - del_3) % 3][j]
        pk[del_3][step_2] += 1
    print(co)
