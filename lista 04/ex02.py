nmalun=int(input("Digite o número de alunos: "))
i = 0
total = 0

while i <= nmalun:
    nota = int(input("Digite a sua nota: "))
    total +=nota
media = total/nmalun       
print("A média de nota é "+str(media))
