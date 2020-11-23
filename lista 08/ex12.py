def comparar(lista):
    ocorrencias = 0
    historico=[]
    produtos=[]
    for x in range(0,len(lista)):  
        ocorrencias = 0
        if lista[x] not in historico:
            for b in lista:
                if lista[x] == b:
                    ocorrencias+=1      
            produtos.append((lista[x],ocorrencias))
            historico.append(lista[x])
    return produtos
    
lista =['a', 'e', 'b', 'a', 'c', 'a','b', 'a', 'e']
print(comparar(lista))
