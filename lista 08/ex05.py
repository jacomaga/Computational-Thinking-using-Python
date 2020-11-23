 
n = int(input("Digite um número: "))
lista = []
valor = 0
for i in range(0,n):
    valor = float(input("Digite um número: "))
    lista.append(valor)
maior = 0
crescente = "" 
i =0

while i < len(lista)-1:
    if  lista[i] < lista[i+1]:
        crescente = "Essa lista é crescente"
     
    else:
        crescente = "Essa lista não é crescente"
        break

    i+=1
    
print(crescente)
