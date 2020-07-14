def fatorial(n):

    if ((n == 1) or (n == 0)):
        return 1
    else:
        return fatorial(n - 1) * n

while True:
    try:
        a, b = map(int, input().split())
        print(fatorial(a) + fatorial(b))
    except EOFError:
            break