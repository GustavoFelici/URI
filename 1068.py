while True:
    n= str(input())
    k=0
    j=0
    for i in range (0,len(n)):

        if(n[i] == '('):
            k = k + 1
        elif(n[i] == ')' and k > j):
            j = j + 1
    if(k == j):
        print("correct")
    else:
        print("incorrect")
