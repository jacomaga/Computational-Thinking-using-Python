##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2017
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Primeira reimpressão - Outubro/2011
# Segunda reimpressão - Novembro/2012
# Terceira reimpressão - Agosto/2013
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Primeira reimpressão - Segunda edição - Maio/2015
# Segunda reimpressão - Segunda edição - Janeiro/2016
# Terceira reimpressão - Segunda edição - Junho/2016
# Quarta reimpressão - Segunda edição - Março/2017
# Terceira Edição - Janeiro/2019
#
# Site: http://python.nilo.pro.br/
#
# Arquivo: exercicios\capitulo 05\exercicio-05-28.py
##############################################################################

# Exercício 5.27
# Solução alternativa, usando apenas inteiros
n = int(input ("Digite o número a verificar:"))
# Com n é um número inteiro, vamos calcular sua
# quantidade de dígitos, encontrado a primeira
# potência de 10, superior a n.
# Exemplo: 341 - primeira potência de 10 maior: 1000 = 10 ^ 4
# Utilizaremos 4 e não 3 para possibilitar o tratamento de números
# com um só dígito. O ajuste é feito nas fórmulas abaixo
q = 0
while 10 ** q < n:
    q = q + 1
    
i = q
f = 0
numerofinal = numeroinicial = numero 
pi = pf = 0 
while i > f:
    posicaoinicial = int(numeroinicial / (10 ** (i-1))) # Dígito mais à direita
    print(posicaoinicial)
    posicaofinal = numerofinal % 10                 # Dígito mais à esquerda
    print(posicaofinal)
    if posicaoinicial != posicaofinal: # Se são diferentes, saímos
        break
    f = f + 1 # Passamos para o próximo dígito a esqueda
    i = i - 1 # Passamos para o dígito a direita seguinte
    numeroinicial = numeroinicial - (posicaoinicial * (10 ** i )) # Ajustamos ni de forma a retirar o dígito anterior
    numerofinal = int(numerofinal / 10) # Ajustamos nf para retirar o último dígito
   

if posicaoinicial == posicaofinal:
    print("%d é palíndromo" % n)
else:
    print("%d não é palíndromo" % n)