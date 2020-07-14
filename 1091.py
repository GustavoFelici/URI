k=int(input())

while k!=0:

    n,m = map(int,input().split())

    for i in range(0,k) :

        x,y = map(int,input().split())


        if (x>n and y>m):
            print("NE")

        elif(x>n and y<m):
            print("SE")
        elif(x<n and y>m):
            print("NO")
        elif(x<n and y<m):
            print("SO")

        else:
            print("divisa")

    k=int(input())
