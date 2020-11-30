# Alternativa A
def contadigitos(n,d):
    aparecimentos = 0
    while n!=0:
        if n%10 == d:
            aparecimentos +=1
        n = n//10
    return aparecimentos

a = 1234
b = 4321
# Alternativa B
def permutacao(a,b):
    while a!=0:
        permutacaoo = False
        if contadigitos(b,a%10) == 0:
           return False
        elif(contadigitos(b,a%10)<contadigitos(a,a%10)):
            return False
        else:
            print(a)
            a = a//10
            permutacaoo = True
    return permutacaoo
            
        
print(permutacao(a,b))
    