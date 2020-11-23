hut = int(input("Digite o número de horas úteis do seu mês"))
hutm = int(input("Digite o número de horas úteis do seu mês: "))
hutd = int(input("Digite o número de horas trabalhadas: "))
vhr = int(input("Digite o valor da sua hora: "))
hrx = hutm - hutd
vhrx = hrx*(vhr*1.5) 


if hutd > hutm:
    print("Você ganhou "+str(vhrx)+" reais de horas extras")
    print("Seu salário final é "+str(vhrx+(vhr*hutd)))
else:
    print("Seu salário final é "+str(vhr*hutd))