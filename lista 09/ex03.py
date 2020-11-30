import random
lista=[ i for i in range(0,10)]
blacklist=[2,1,3,4,5,6,7,8]
def removeritens(lista,blacklist):
    
    contador = len(lista)-1 

    while contador > 0:
        
        if lista[contador] in blacklist:
            lista.remove(contador)
            contador = len(lista)-1
        
        else:
            contador -= 1 

    return lista

print(removeritens(lista,blacklist))
