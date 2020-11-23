
#variaveis necessárias apenas no ex 03
#frase = input("Digite uma frase: ")
#letra = input("Digite uma letra para ser substituída na frase: ")

def substituir (frase, letra):
    
    letra = letra.lower()
    posicoes = list()
    newfrase=[]
   
    for i in range(len(frase)):
        if frase[i].lower() != letra:
            newfrase = newfrase+list(frase[i])
        else:
            newfrase.append("*")

    frase = "".join(newfrase)
    return frase


