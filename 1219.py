from math import sqrt
pi = 3.1415926535897

while True:
    try:
        a,b,c = map(int, input().split())
        p = (a+b+c)/2
        at = sqrt(p*((p-a)*(p-b)*(p-c)))

        # AB = c | AC = b | CB = a | Base = c

        raiom = (a*b*c)/sqrt((a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c)) #fonte https://www.mathopenref.com/trianglecircumcircle.html
        rm = pi*(raiom**2)
        s = rm - at

        raio = 2*a/p  #fonte https://www.mathopenref.com/triangleincircle.html
        r = pi*(raio**2)

        v = at - r

        print("{0:.4f}".format(s),"{0:.4f}".format(v),"{0:.4f}".format(r))

    except EOFError:
            break

#Quase... segundo caso está dando erro.