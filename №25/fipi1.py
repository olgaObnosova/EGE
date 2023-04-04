import  fnmatch as f
for i in range(123454, 10**8):
    if f.fnmatch(str(i),'1234*54') and i%21==0:
        print(i, i//21)