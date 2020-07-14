n = int(input())
while n>0:
    n-=1
    x = input().split()
    x.sort(key=len, reverse=True)
    f = ''
    for i in range (len(x)):
        f += x[i] + ' '
    print(f)