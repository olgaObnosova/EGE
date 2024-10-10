for x in '0123456789abcdefghijkl':
    a= int(f'98{x}79641',22)+int(f'36{x}14',22)+\
        int(f'73{x}4', 22)
    if a%21==0:
        print(int(x,22), a//21)
