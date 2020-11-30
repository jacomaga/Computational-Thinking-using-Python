def primo(valor):
    div = 0
    i = 1
    while i <= valor  :
        if valor % i == 0 :
            div += 1
        i+=1
    if div == 2:
        return valor
    

for x in range(0,100):
    if primo(x) == True:
        print(x)
    
    