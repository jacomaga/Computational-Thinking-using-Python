frase = input("Digite uma frase:")
palavra = input("Digite o termo da busca:")


def encontrar(frase,palavra):
    frase = frase.lower()
    palavra = palavra.lower()
    palavra_len = len(palavra)
    contador = 0
    for i in range(len(frase)):
        if frase[i:i+palavra_len] == palavra:
            contador+=1
    
    return contador
print(encontrar(frase,palavra))
#https://stackoverflow.com/questions/8899905/count-number-of-occurrences-of-a-given-substring-in-a-string
#https://python-reference.readthedocs.io/en/latest/docs/str/count.html
