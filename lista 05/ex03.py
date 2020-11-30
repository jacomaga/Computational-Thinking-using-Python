def perfeito(valor):
    stack = 0
    for i in range(1,valor):
        if valor % i == 0:
            stack += i
    if stack == valor:
            return True    

for i in range(0,50000):        
    if perfeito(i) ==  True:
        print(i)