def fatorial(n):
    x = 2
    acumulador = 1
    while x <= n:
        acumulador *= x
        x+=1          
    return acumulador          

def numerocombinacoes(n,p):
    
    nmenosp=fatorial((n-p))
    n = fatorial(n)
    p = fatorial(p)
    ncombinacao = n/(nmenosp*p)
    return ncombinacao

possibilidades = numerocombinacoes(5,2)

tupla = ("bia", "ana","maria","joana","eva")
nome = 0
combinacao=""
n = len(tupla)-1
while nome < len(tupla):
    
    for i in range(1,len(tupla)):

        if nome < i: 
            combinacao = tupla[nome] +" "+ tupla[i]
            print(combinacao)
    
    nome+=1
    

