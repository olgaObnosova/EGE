s = open("2.txt")
a=[]
c=1
count=0
m=0
sp=[]
for i in s:
  a.append(i)
for i in range(len(a)): 
  h=a[i]
  v=0
  c=1
  for j in range(len(h)): 
    if h[j]=='R':
      v+=1
    if v>=30:
      break
  if v<30:
    for j in range(len(h)-1): 
      for l in range(j+1,len(h)):        
        c+=1
        sp.append(h[l])
        if h[l]==h[j]:
          if c>2:
            print(sp)
            count+=1
            if l-j>m:
              m=l-j   
          c=1
          sp=[]
          break
print(m,count)
