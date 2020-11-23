'''Um número inteiro positivo n é denominado primo se existirem apenas dois divisores inteiros
positivos dele: o 1 e o próprio n. Escreva um algoritmo que recebe um inteiro n e verica
se n é primo ou não.'''
i = 1 
n = int(input("Digite um número: "))
d = 0
while i <= n:
    if n % i == 0:
        d += 1
    i+=1
if d==2:
    print("Esse número é primo")
elif d > 2:
    print("Esse número não é primo")