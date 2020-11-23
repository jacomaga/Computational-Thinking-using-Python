a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
def segmento(a,b):
    maior = 0 
    menor = 0
    subs = False
    if a > b:
        maior = a 
        menor = b
    else:
        menor = a 
        maior = b
    tmenor = len(str(menor))
    while maior > 0: 
        if (maior%(10**tmenor)) == menor%(10**tmenor):
            subs = True
        
        maior = maior//10
    return subs
print(segmento(a,b))