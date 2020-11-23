n = (4,7,8,10,11)

def medias(range):
    stack = 0 
    for i in range:
        stack += i
    media = stack/len(range)
    return media
def raiz(numero):
    x = numero
    raiz = 0
    while x > 0:

        if numero % x != 0:
            print("esse é o x: "+str(x))
            
        elif x != 1 and x ** 2 == numero: 
            raiz = x
        x -= 1
    return raiz

def desviopadrao(rangen):
    desvio = 0
    stack = 0 
    media = medias(rangen)
    for i in rangen:
       stack += (i - media)**2

    desvio = (stack / len(rangen))
    return desvio

print(desviopadrao(n))

