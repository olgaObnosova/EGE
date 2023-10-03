with open('2666_B.txt') as f:
    n=int(f.readline())
    maxx=maxx6=maxx2=maxx3=0
    for line in f:
        x=int(line)
        if x%6==0:
            maxx6=max(maxx6,x)
        elif x%2==0:
            maxx2=max(maxx2, x)
        elif x%3==0:
            maxx3=max(maxx3, x)
        else:
            maxx=max(maxx, x)
print(maxx, maxx6, maxx3, maxx2)
print(max(maxx*maxx6,maxx2*maxx3,maxx2*maxx6, maxx3*maxx6))