for x in range(6):
    for y in range(6):
        if int(f'10{x}{y}{x}',6)==int(f'{y}11{x}',7):
            print(x+y)