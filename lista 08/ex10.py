def intercala(listaa,listab):
    c = listaa+listab
    i = 1
    j = 0
    lp=len(c)-1
    menor = 0
    for index in range(0,len(c)):
        min_index = index
        
        for right in range(index+1,len(c)):
            if c[right]<c[min_index]:
                min_index = right
        c[index],c[min_index] = c[min_index], c[index] 
    
    return c

a=[1,2,3,4,5,6,7,8]
b=[10,2,2,4,88,99,100,200,12,14,9,10,1]
print(intercala(a,b))
                                                
