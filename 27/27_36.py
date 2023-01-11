import operator
f=open('27_36.txt',encoding='utf-8')
word={}
for line in f:
    line=line.rstrip()
    if line in word:
        word[line]+=1
    else:
        word[line]=1
    #word[line]=word.get(line,0)+1
'''
print(word)
list_keys = list(word.keys())
list_keys.sort()
print(list_keys)
for i in list_keys:
    print(i, ':', word[i])
'''
sorted_tuples = sorted(word.items(), key=operator.itemgetter(1))
print(sorted_tuples) 
sorted_dict = {k: v for k, v in sorted_tuples}
print(sorted_dict)

