with open('27.txt') as f:
    n = f.readline()
    pk_ch = [0]
    pk_nech = [0]
    for i in f.readlines():
        if int(i) % 2 == 0:
            pk_ch.append(pk_ch[-1] + 1)
            pk_nech.append(pk_nech[-1])
        else:
            pk_ch.append(pk_ch[-1])
            pk_nech.append(pk_nech[-1] + 1)
    pk_ch = pk_ch[1:]
    pk_nech = pk_nech[1:]
    pk_dif = []
    for i in range(len(pk_ch)):
        pk_dif.append(pk_ch[i] - pk_nech[i])
    # дефолтный код для префиксного массива
