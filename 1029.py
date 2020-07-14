def fibonacci(n):
    global cont
    cont += 1
    if n <= 1:
        return n
    else:

        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input())

for i in range(n):
    x = int(input())
    cont = 0
    resu = fibonacci(x)
    print('fib({}) = {} calls = {}'.format(x, cont-1, resu))

#Time limited