n = int(input())

p = []
im = []
for i in range(0,n):
    x =  int(input())
    if x%2 == 0:
        p.append(x)
    else:
        im.append(x)

p.sort()
im.sort(reverse=True)
for i in range(0,len(p)):
    print(p[i])

for i in range(0,len(im)):
    print(im[i])