def mdc(a,b):
    while b !=0:
        resto = a % b
        a = b
        b = resto

    return a

n = int(input())

for i in range(0,n):
    f1, f2 = map(int, input().split())
    print(mdc(f1,f2))
