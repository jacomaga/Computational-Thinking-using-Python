import random
n = int(input("Digite a quantidade de números: "))
lista = []
valor = 0
for i in range(0,n):
    valor =random.randint(1,1000)
    lista.append(valor)
print(lista)
