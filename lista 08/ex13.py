portas = [False] * 1001
def passagem (lista,porta):
    i = porta

    while i < len(lista):
        valor = i
        if lista[valor] == False:
            lista[valor] = True
        else:
            lista[valor] = False
        lista[i]
        i+=porta
    return lista
retorno = passagem(portas,5)
for i in range(1,len(retorno)):
    if retorno[i] == True:
        print("Porta aberta" + str(i))
         

