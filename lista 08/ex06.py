lista = [1,2,3,4,5,6,9]
i = 0
n = int(input("Insira um número: "))

while i < len(lista) and n > lista[i]:
    i = i +1
lista.insert(i,n)

   
print(lista)
