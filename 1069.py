k =  int(input());

for j in range(0,k):
    nome = str(input())
    cont = 0
    cont2 = 0

    for i in range(0,len(nome)):

        if(nome[i] == '<'):
            cont = cont + 1

        elif not nome[i] != '>' and cont > cont2:
            cont2 = cont2 + 1

    if(cont > cont2):
        resu = cont2
    elif(cont < cont2):
        resu = cont
    else:
        resu = cont

    print(resu)