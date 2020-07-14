import math
i=0
r = int(input())
if(r != 0):
    while True:

        if (r == 0):
            break
        w,l = map(int,input().split())

        i+=1
        m = 2*r
        a = math.sqrt((w**2)+(l**2))


        if(a<=m):
            print("Pizza",i,"fits on the table.")
        else:
            print("Pizza",i,"does not fit on the table.")
        r = int(input())

#problema na entrada