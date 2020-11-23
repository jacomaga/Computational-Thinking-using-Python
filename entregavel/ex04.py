#receber dois numeros e calcular o mdc maior divisor comum
a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
if a <= 0 or b <= 0:
    print("Digite números positivos!")
else:
    if a>b:
        maior = a
        menor = b
    else:
        maior = b
        menor = a
    cont = maior
    while cont >0:
        if (maior % cont == 0) and (menor % cont == 0):
            mdc = cont 
            print(mdc)
            break
        cont-=1    

