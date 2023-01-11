f=open('25006980.txt')
s=f.readline()
print(s[0])
count=0
for i in range(len(s)-3):
    if s[i]=='Z' and s[i+2]=='R' and s[i+3]=='O':
        count+=1
print(count)
