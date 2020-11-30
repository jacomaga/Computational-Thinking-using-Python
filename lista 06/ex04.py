import substituir from ex03 
frase = input("Digite uma frase: ")
caracteres = input("Digites os caracteres que quer substituir: ")
caracteres = list(caracteres)
for i in range (len(caracteres)):
    frase = substituir(frase, caracteres[i])

print(frase)
