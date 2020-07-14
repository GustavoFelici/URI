x,y,n = map(int,input().split())
resu = ""
for i in range (n):
    xi,yi,ti = map(int,input().split())
    d = ((x-xi)**2)+((y-yi)**2)

    if(d < ti**2):
        if(len(resu) == 0):
            resu = str(i+1)
        else:
            resu = resu +" "+str(i+1)

if(resu == ""):
    print("-1")
else:
    print(resu)