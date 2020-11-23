#def ordena(vetor):
#    i=1
#    while i<len(vetor):
#        j=i
#        while j>0 and vetor[j] < vetor[j-1]:
#            aux = vetor[j]
#            vetor[j] = vetor[j-1]
#            vetor[j-1] = aux
#            j=j+1

v=[2,3,5,8,10,12,4]
#print(ordena(v))

def recursao(n):
    if n  <= 10:
        return  n * 2
    else:
        valor = recursao(n / 3)
        return recursao(valor)
print(recursao(27))

