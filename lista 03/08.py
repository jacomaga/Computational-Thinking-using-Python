numA = float(input(" Digite um numero : "))
numB = float(input(" Digite um outro numero : "))
op = input (" Operador (+ -*/) : ")
soma = ( op == "+")
subtracao = ( op == "-")
multiplicacao = ( op == "*")
divisao = ( op == "/")
if soma :
    resultado = numA + numB
elif subtracao :
    resultado = numA - numB
elif multiplicacao :
    resultado = numA * numB
elif divisao :
    if numB == 0:
        print("Essa operação é impossível")
    else:
        resultado = numA / numB    


print (" Resp : {}". format ( resultado ))
