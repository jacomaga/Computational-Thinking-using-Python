# carta = numero e naipe
#numero de cartas 4 ~ ...[Q,J,K]... 3 = 10 cartas
#numero de naipes = 4
import random

cartaX = [random.randint(0,9),random.randint(0,3)]
cartaY = [random.randint(0,9),random.randint(0,3)]

def comparar(cartaX,cartaY):

    if cartaX[0] > cartaY[0]:
        return -1
    elif cartaX[0] == cartaY[0]:
        if cartaX[1] > cartaY[1]:
            return -1
        elif cartaX[1] == cartaY[1]:
            return 0
        else:
            return 1
    else:
        return 1

print("As cartas são:"+str(cartaX)+","+str(cartaY))
print(comparar(cartaX,cartaY))
