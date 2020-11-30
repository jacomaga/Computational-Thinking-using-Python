'''Dados um montante em dinheiro inicial d, uma taxa de juros mensal j e um período de
tempo em meses t, escreva um algoritmo que calcula o valor nal em dinheiro se d car
aplicado a taxa de juros j durante t meses.'''
d = int(input("Digite o montante: "))
j = int(input("Digite o juros mensal: "))
t = int(input("Digite o tempo: "))
i = 0
while i < t:
    d = d+j/100*d
    print(d)
    i+=1
print(d)