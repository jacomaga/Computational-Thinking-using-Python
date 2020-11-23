m1 = int(input("Digite a sua média do primeiro semestre: "))
m2 = int(input("Digite a sua média do segundo semestre: "))
mf = m1*4+m2*6/10
am = 100
af = int(input("Digite o seu número de faltas: "))
aulasass = am - af

# x = aulasass*100/am 

fq =  aulasass*100/am 
print("Sua média final é "+str(mf))
print("Sua frequência é de "+str(fq)+"%.")

if fq>=70 and mf>=6:
    print("Você foi aprovado.")
else:
    print("Você foi reprovado.")