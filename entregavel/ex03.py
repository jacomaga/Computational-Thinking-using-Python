#receber dois números e calcular o MMC
a = int(input("Digite um número positivo: "))
b = int(input("Digite outro número: "))
if a <= 0 or b <= 0:
    print("Digite números positivos!")
else:
    if a>b:
    maior = a
    menor = b
    else:
        maior = b
        menor = a
    for i in range(1,maior):
        sup = menor * i
        if sup%a == 0 and sup%b==0:
            mmc = sup
            print("O MMC é {0}".format(mmc))
            break

