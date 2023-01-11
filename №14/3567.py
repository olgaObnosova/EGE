for i in range(128,256):
    a=oct(i)[2:]# восьмеричная
    b=bin(i)[2:]#2
    c=hex(i)[2:]#16
    if b[0]+b[1]=='10' and a[1]=='4' and c[-1]=='2':
        print(i)
    
