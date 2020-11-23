idd=int(str("Digite sua idade, caro nadador: "))
infantil = (idd>=5 & idd<=7)
juvenil = (idd>=8 & idd<=10)
adolescente = (idd>=11 & idd <=15 )
adulto = (idd>=16 & idd <=30) 
senior = (idd>30) 

if infantil:
    print("Sua categoria é infantil")
elif juvenil:
    print("Sua categoria é Juvenil")
elif adolescente:
    print("Sua categoria e Adolescente")
elif adulto:
        print("Sua categoria e Adulto")
elif senior:
        print("Sua categoria e Sênior")
else:
    print("Você não tem idade suficiente para participar")                
