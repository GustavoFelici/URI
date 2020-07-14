def move(n):
    aux = n[0]
    n.pop(0)
    n.append(aux)

while True:
    x = int(input())

    if x == 0:
        break

    discarded = []

    n = list(range(1,x+1))
    while True:
       if len(n) == 1:
           break
       discarded.append(n[0])
       n.pop(0)
       move(n)

    sdiscarded = [str(a) for a in discarded]
    n = str(n[0])
    print('Discarded cards:',", " . join(sdiscarded))
    print('Remaining card:',n)