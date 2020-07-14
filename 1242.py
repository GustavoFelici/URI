while True:
    try:
        # entre as bases B e S e as bases C e F.
        f = str(input())
        midle = int(len(f)/2)
        f1 = f[0:midle]
        f2 = f[midle:len(f)]
        x=0

        for i in range (0,min(len(f1),len(f2))):
            if f1[i] == 'B' and f2[i] == 'S' or f1[i] == 'S' and f2[i] == 'B' or f1[i] == 'C' and f2[i] == 'F' or f1[i] == 'F' and f2[i] == 'C':
                x+=1

        print(x)
    except EOFError:
     break