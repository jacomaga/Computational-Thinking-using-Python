n = int(input("Digite um valor n: "))
listat=[]
def listaxnmrs(qntd):
    valor=""
    lista=[]
    for i in range(0,qntd):
        valor =float( input("Digite um valor: "))
        lista.append(valor)
    return lista
listat = listaxnmrs(n)
i = 0
y = len(listat)-1
while i <=  y:
    print(listat[i]+listat[y])
    y-=1
    i+=1

        
