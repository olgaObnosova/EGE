f=open('24-1.txt')

n=0

while True:

    s=  f.readline()

    flag=0

    for i in range (0,len(s)-3):

        if s[i]=='Z' and s[i+2]=='R'  and s[i+3]=='O':

            flag=1

            if flag==1:

                n+=1

                break

    if not s:

        break

f.close()

print(n)
