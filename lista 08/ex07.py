lista = [2.3,3.2,1.5,2.2,3.3,5.5,6.6,7.7,8.8]
n = float(input("Digite um número real: "))
i = 0
ac = 0
while i < len(lista)-1:
    if lista[i] >= n:
        ac +=1
    i+=1
print(ac)
