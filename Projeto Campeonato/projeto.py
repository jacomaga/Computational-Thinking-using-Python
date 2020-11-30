import random
# Time - id, pontos, vitórias e gols

#Exercício 01

time=[["nome: ", 0],["jogos: ", 0]]

#Exercício 02 
def criarTimes(quantidade):
    times=[]
    
    for auxiliar in range(quantidade):
        times.append([["Nome:",auxiliar],["Jogos",0],["Pontos:",0],["Vitórias:",0],["Gols:",0]])
    return times
times=criarTimes(10)


#Exercício 03
#vitoria = 3 pontos | empate = 1 pontos 

def partida(timeA,timeB):
    
    golsA=random.randint(0,5)
    golsB=random.randint(0,5)   
    
    
    if golsA > golsB:
        #Soma gols
        timeA[4][1]+=golsA
        timeB[4][1]+=golsB
        #Vitoria
        timeA[3][1]+=1
        #Pontos
        timeA[2][1]+=3
        #Jogos
        timeA[1][1]+=1
        timeB[1][1]+=1
        
    elif golsA == golsB:
        #empate 
        timeA[2][1]+=1
        timeB[2][1]+=1
        #somagols
        timeA[4][1]+=golsA
        timeB[4][1]+=golsB
        stpartida = False
        #Jogos
        timeA[1][1]+=1
        timeB[1][1]+=1 
    else:
        #Soma gols
        timeA[4][1]+=golsA
        timeB[4][1]+=golsB
        #Vitoria
        timeB[3][1]+=1
        #Pontos
        timeB[2][1]+=3
        stpartida=False
        #Jogos
        timeA[1][1]+=1
        timeB[1][1]+=1
    participantes=[timeA,timeB]
    return participantes

#Exercício 04
def imprimirTime(listaTimes,campeao):
    for item in listaTimes:
        print(item[0])
        print(item[1])
        print(item[2])
        print(item[3])
        print(item[4])
        print("---------------------")

def ordenarTimes(listaTimes):
    
    tLista = len(listaTimes)

    for indiceAd in range(1,tLista):

        chave = listaTimes[indiceAd][2][1]
        aux =  indiceAd - 1
    
        while aux >= 0 and listaTimes[aux][2][1] < chave:
            
            listaTimes[aux+1],listaTimes[aux] = listaTimes[aux],listaTimes[aux+1]
            aux -= 1
  
         
    print("---------------------------TABELA DE PONTOS---------------------------")
    for indTime in range(0,len(listaTimes)):
        print("{0}º Posição: {1}".format(indTime+1,listaTimes[indTime]))
    
    print("-------------------------------------------------")
    print("O CAMPEÃO É O TIME "+str(definircampeao(listaTimes)[0][1])) 
           
#Exercício 05 - Metódo para encontrar o campeão
def definircampeao(times):
    campeao=[]
    maispontos=0
    for time in times:
        if time[2][1]>maispontos:
            campeao=time
            maispontos=time[2][1]

        elif time[2][1]==maispontos:
            if campeao[3][1] < time[3][1]:
                campeao = time

            elif campeao[3][1] == time[3][1]:
                if campeao[4][1]<time[4][1]:
                    campeao = time

                elif campeao[4][1] == time[4][1]:
                    campeao=times
    return campeao

#Método do campeonato
def campeonato(times):
    rodadas = []
    for timeAlvo in range(0,len(times)):
        for timeAdversario in range(0,len(times)):
            if timeAlvo != timeAdversario:
                resultadoPartida = partida(times[timeAlvo],times[timeAdversario])
                times[timeAlvo] = resultadoPartida[0]
                times[timeAdversario] = resultadoPartida[1]
                times[0][1][1] 
    ordenarTimes(times)
       
campeonato(times)

