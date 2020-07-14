def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

n,m,l,r = input().split()
n = int(n)
m = int(m)
l = int(l)
r = int(r)

resu1 = fatorial(n*m)
resu2 = fatorial(l)
resu3 = fatorial(r)

print(n,m,l,r,resu1/(resu2*resu3))