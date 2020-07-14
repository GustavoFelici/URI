while True:
    try:
        x,y = map(int,input().split())
        m1 = max(x,y)
        m2 = min(x,y)

        print(m1-m2)

    except EOFError:
            break