'''Dados n um inteiro positivo e uma sequência de n números reais, escreva um algoritmo que
conta e imprime a quantidade de números positivos e a quantidade de números negativos.'''
n  = int(input("Informe o tamanho da sequencia:"))
cn = 0
cp = 0
i = 0 
while i <= n:
    num = float(input("Informe um valor: "))
    if num<0:
        cn += 1
    elif num > 0:
        cp +=1
    i += 1
