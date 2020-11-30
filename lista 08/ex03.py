lista = []
valor = ""
for i in range(0,10):
    valor = input("Digite uma mensagem: ")
    lista.append(valor)

for i  in range((len(lista)-1),0,-1):
    print (lista[i])
