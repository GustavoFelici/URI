n = int(input())
for x in range (0,n):
    c = float(input())
    i = 0
    while True:
        if c > 1:
            c = c - (c / 2)
            i += 1
        else:
            break
    print(i, 'dias')

