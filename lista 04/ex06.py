'''Em uma prova de concurso com 70 questões haviam 20 pessoas concorrendo. Sabendo que
cada questão vale 1 ponto, escreva um algoritmo que lê a pontuação da prova obtida de cada
um dos candidatos e calcula:
a) a maior e a menor nota
b) o percentual de candidatos que acertaram até 20 questões, o percentual que acertaram
de 21 a 50 e o percentual que acertou acima de 50 questões'''

nota = int(input("Digite a sua nota:"))
i = 0
maior = nota
menor = nota
while i <= 19:
    nota = int(input("Digite a sua nota:"))
    if nota > maior:
        maior = nota
    elif nota < menor:
        menor = nota
    i += 1
    
    

        