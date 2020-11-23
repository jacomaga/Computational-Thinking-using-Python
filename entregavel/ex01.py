total = 0
print("Categorias: \n1- Camisetas e polos \n2- Calças e camisas\n3- Jaquetas e Agalhasalhos \n4- Ternos e sobretudos")
for i in range(4):
    i+=1
    valor = float(input("Digite o valor do tipo de produto in {0}: ".format(i)))
    
    if i == 1:
        camisetaepolo = valor*0.04
        total += camisetaepolo
        
    if i == 2:
        calcaecamisa = valor*0.055
        total += calcaecamisa 
        
    if i == 3:
        jaquetaeagasal = valor*0.07
        total += jaquetaeagasal
       
    if i == 4:
        ternoesobre= valor*0.085
        total +=  ternoesobre
   
total+=500    
print(total)    
    
    