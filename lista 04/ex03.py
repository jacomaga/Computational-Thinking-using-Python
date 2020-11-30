nmalun=int(input("Digite o número de alunos: "))
i = 0
total = 0
fum=0
fdois=0
while i <= nmalun:
    nota = int(input("Digite a sua nota: "))
    total +=nota
    if nota < 5:
        fum += 1
    elif nota >= 5:
        fdois += 1 
    i += 1
media = total/nmalun       

