'''Escreva um algoritmo que, dados um número inteiro positivo n, 
imprime na tela a contagem de todos os divisores positivos de n.'''

x = int(input("Digite um número: "))
i = 0
div = 0  
while i <= x:
    if i % 0:
        div += 1 
    i += 1
print("O número total de divisores é "+str(div))
