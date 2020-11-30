'''A conversão de graus Fahrenheit para centígrados é obtida pela fórmula C = 5
9 (F 􀀀 32).
Escreva um algoritmo que calcule e escreva uma tabela de graus centígrados em função de
graus Fahrenheit que variem de 50 a 150 Fahrenheit de 1 em 1.'''
i = 50
while i <= 150:
    c = (i - 32)/9*5
    print(str(i)+" Fahrenheit em celsius é "+str(c)) 
    i+=1
