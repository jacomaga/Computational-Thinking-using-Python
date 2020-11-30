n = int(input("Digite um número: "))
i= 2
n1 = 0
n2 = 1
t =0
while i <=n:
    t = n1+n2
    n1 = n2
    n2 = t
    i+=1
print(t)