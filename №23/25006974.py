def F(start, finish):
    if start == finish:
        return 1
    elif start > finish or start==11 or start==18:
        return 0
    else:
        return F(start+1, finish)+F(start+2, finish)+F(start*3, finish)
print(F(4, 8)*F(8,23))
