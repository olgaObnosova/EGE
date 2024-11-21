import re as re
with open('24_17878.txt') as f:
    f = f.readline()
sp=re.findall(r'(?:\d+[-*]?)*', f) \
    #(r'(?:0|[6-9][06-9]*)(?:[-*](?:0|[6-9][06-9]*))*', s)
print(sp[:4])
    
