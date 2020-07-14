b = str(input())
s = int(input())
i=0
r=0
c=0
while True:

    if(c == s):
        break
    if (len(b) == i):
        c+=1
        i=0
    if (b[i] == 'E' and c == 0):
        r += 1
        print("entrou1")
    if ((b[i] != b[i-1] and c > 0)  or (i==0 and b[i]!=b[len(b)-1])):
        print(i)
        r += 1
        print("entrou2")

    i += 1
print(r)
#Não termininado
