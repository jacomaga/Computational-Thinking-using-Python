import random
lista=[ i for i in range(0,10)]
def embaralhar(lista):
    usados=[]
    
    while len(usados)<len(lista):
        numeroum = random.randint(0,9)
        numerodois = random.randint(0,9)
        if numeroum and numerodois not in usados:
            lista[numeroum],lista[numerodois] = lista[numerodois],lista[numeroum]
            usados.append(numeroum)
            usados.append(numerodois)
    return list

        
print(embaralhar(lista))
