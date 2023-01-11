Graph ={
    'А':'ГБ',
    'Б':'Д',
    'В':'АБГД',
    'Г':'ЕЖ',
    'Д':'ЕИК',
    'Е':'ВК',
    'Ж':'Е',
    'И':'К',
    'К':'Л',
    'Л':'ЕЖ',
}

start='Е'
finish='Е'

N=0
ways=[start]
while len(ways)>0:
    w = ways[0]
    del ways[0]
    f = w[-1]
    for x in Graph[f]:
        if x == finish:
            print(w+x)
            N = N+1
        else:
            ways.append(w+x)
print(N)