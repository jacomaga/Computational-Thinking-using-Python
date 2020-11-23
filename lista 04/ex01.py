on = true
total=0
while on == true:
    x = int(input("Digite um número:"))    
    if(x != 0) and x % 2 == 0:
        total += x 
    else:
        on = false
