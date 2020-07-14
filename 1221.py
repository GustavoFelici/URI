import math

def primo(n):
    if n%2 == 0 and n>2:
        return False
    return all(n%i for i in range(3,int(math.sqrt(n))+1, 2))

n = int(input())

for i in range (0,n):
    x =int(input())

    if(primo(x)):
        print("Prime")
    else:
        print("Not Prime")