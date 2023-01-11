def f(start, stop, n, lst):
    
    if (start > stop) or (n > 2):
        return 0
    elif start == stop:
        return 1
    else:
        return f(start + 1, stop, n * int(lst == 0) + 1, 0) \
               + f(start * 2, stop, n * int(lst == 1) + 1, 1)
        
        
print(f(1, 14, 0, 2))
