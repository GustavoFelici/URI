def mdc(num1, num2):
    resto = None
    while resto is not 0:
        resto = num1 % num2
        num1  = num2
        num2  = resto

    return num1

n = int(input())

while n>0:
    n -= 1
    o = str(input())
    o = o.split()

    N1 = float(o[0])
    D1 = float(o[2])
    N2 = float(o[4])
    D2 = float(o[6])

    if o[3] == '+':
       r1 = (N1 * D2) + (N2 * D1)
       r2 = D1 * D2
    elif o[3] == '-':
        r1 = (N1*D2) - (N2*D1)
        r2 = (D1*D2)
    elif o[3] == '*':
        r1 = (N1*N2)
        r2 = (D1*D2)
    elif o[3] == '/':
        r1 = (N1*D2)
        r2 = (N2*D1)

    r1 = int(r1)
    r2 = int(r2)
    x = int(mdc(r1,r2))
    print(str(r1)+'/'+str(r2),'=',str(int(r1/x))+'/'+str(int(r2/x)))