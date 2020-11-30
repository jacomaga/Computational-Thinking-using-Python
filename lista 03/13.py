dia = int(input("Digite o número do dia:"))
mes = int(input("Digite o número do mês:"))
ano = int(input("Digite o ano: "))
if dia > 0 and dia <=31:
    print("Esse dia é existente")
else:
    print("Esse dia não existe")
if mes >0 and mes <=12:
    print("Esse é um mes existente")
else:
    print("Esse dia não é existente")
if mes == 2 and dia > 28:
    print("Esse dia não existe nesse mês")
elif mes%2==0 and mes!=2 and dia > 30:
    print("Esse dia não existe nesse mês")
elif ano%4==0 and ano%100!=0 and mes == 2 and dia > 29:
    print("Esse dia não existe nesse ano")
else:
    print("Essa data é válida")