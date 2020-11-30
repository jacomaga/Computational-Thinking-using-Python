times = ["Alemanha","Argentina","Bélgica","Brasil","Colômbia","Costa Rica","França","Holanda"]
combinacao = ""
for i in range(0,len(times)):
    for j in range(i+1,len(times)):
        if i < j:
            combinacao = times[i]+ " "+ times[j]
            print(combinacao)

