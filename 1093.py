while True:
    ev1,ev2,at,d = map(int,input().split()) #probablidade do vampiro 1 ganhar
    if(ev1 == 0 and ev2 == 0 and at == 0 and d == 0):
        break

    #probabilidade do dado ser menor igual ao AT
    prob = at/6
    i=0
    while (ev2 - d > 0):
        ev2 -= d
        prob*=prob
        i+=1
    print(prob*100,i)