import math
a = float(input("Digite o valor de A: "))   
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
if a!=0:
    delta = (b**2)-4*a*c
    rd = float(delta)**0.5
    x1=(b*-1 + rd)/2*a
    x2=(b*-1 - rd)/2*a
    print(str(x1))
    print(str(x2))

else:
    print("O valor de A é zero, logo a operação não possuí resolução completa")