listqt = []
listpeso = []
soma_qt = 0
soma_peso =0
n = int(input())

for i in range(0,n):
    pac = int(input())
    for j in range(0,pac):
        qt,peso = map(int,input().split())

        listqt.insert(j,qt)
        listpeso.insert(j,peso)
        listqt.sort()
        listpeso.sort()
        for k in listqt:
            soma_qt += k
        for l in listpeso:
            soma_peso += l
    print(soma_qt,soma_peso)