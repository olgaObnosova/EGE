with open('27-18b.txt') as In:
    In = list(map(int, In.readlines()))
    Length = In.pop(0)

D = 0

for i in range(len(In) - 4):
    for j in range(i + 1, i + 5):
        if (In[i] + In[j]) % 2 != 0 and (In[i] * In[j]) % 13 == 0:
            D += 1

print(D)
