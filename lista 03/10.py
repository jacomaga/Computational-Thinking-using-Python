valor = int(input("Digite o valor do produto: "))
meio = input("Digite o meio de pagamento cartão, dinheiro ou cheque: ")
parc = input("Irá parcelar? digite s para sim ou n para não: ")
vdc = (parc == "n" and (meio == "dinheiro" or meio == "cheque"))
vcr =  (parc == "n" and (meio == "cartão"))

if parc == "s":
    vzparc = int(input("Digite o número de parcelas, apenas duas ou quatro vezes: "))

dvparc = (vzparc == 2)
qvparc = (vzparc == 4)   
if vdc:
    vf = valor - (valor * 0.10)
elif vcr:
    vf = valor - (valor * 0.05)
elif dvparc:
    vf = valor
    vp = valor/2
elif qvparc:
    vf = valor + (valor*0.07)
    vp = vf/4       
   