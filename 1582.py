def mdc(a,b):
    while b !=0:
        resto = a % b
        a = b
        b = resto

    return a

while True:
    try:
        x,y,z = map(int, input().split())

        if(z**2 == x**2 + y**2 or y**2 == x**2 + z**2 or x**2== y**2 + z**2):
            m1 = max(x, y, z)
            if (m1 == x):
                m2 = max(y, z)
                rest = min(y, z)
            elif (m1 == y):
                m2 = max(x, z)
                rest = min(x, z)
            elif (m1 == z):
                m2 = max(x, y)
                rest = min(x, y)

            mdc1 = mdc(m1, m2);

            f = mdc(mdc1, rest)

            if(f == 1):
                print("tripla pitagorica primitiva")
            else:
                print("tripla pitagorica")
        else:
            print("tripla")

    except EOFError:
            break