time1 = input("Digite o nome do seu time: ")
time2 = input("Digite o nome do outro time: ")
gols1 = int(input("Digite o número de gols do primeiro time: "))
gols2 = int(input("Digite o número de gols do segundo time: "))
if gols1>gols2:
    print("O "+time1+" ganhou")
    if gols1==gols2:
        print("EMPATE")
else:
    print("O "+time2+" ganhou")
