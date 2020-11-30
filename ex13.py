lista = [False]*1001
def passagem(lista):

    for passageiro in range(1,1001):

        for indice in range(passageiro, len(lista),passageiro):

            if lista[indice] == False:
                lista[indice] = True

            else:
                lista[indice] = False
            for item in range(1,len(lista)):
                if lista[item] == True:
                     lista[item] = "Porta:" + str(item)+ " está aberta "



    return lista


print(passagem(lista))

