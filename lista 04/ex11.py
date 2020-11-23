n = int(input("Digite um número: "))
i = 1
d = 1
while i < n:
    if n%i == 0 and i!=1 and i!=n:
       d = i
    i+=1
if d!= 1 and d!=n:
    print("Esse número não  é primo")
else:
    print("Esse número é primo")