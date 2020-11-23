dia = int(input("Digite um número: "))
mes = int(input("Digite um número: "))
ano = int(input("Digite um número: "))

def data (a,b,c):
    diavalido = False
    mesvalido = False
    anovalido = False
    
    if dia <=31 and dia >= 1:
        diavalido = True
    if mes <= 12 and mes >=1:
        mesvalido = True
    if ano >= 1:
        anovalido = True
    
    if diavalido == False or mesvalido == False or anovalido == False:
        return False
    else:
        return True
    
print(data(dia,mes,ano))