
n = int(input("Digite o valor de n: "))
div = 0
i = 1
while i <= n  :
    if n % i :
        div += 1
    i+=1
if div > 2:
        print("é primo")
else:
    print("não é primo")