a = [1,2,3,4,6,7,8,22,10]
b = [2,3,4,22,23,8]
c = []
rmenor = len(a) if len(a)<len(b) else len(b)
rmaior = len(a) if len(a)>len(b) else len(b)
menor = a if len(a)<len(b) else b
maior = a if len(a)>len(b) else b
for i in range(0,rmaior):
    for x in range(0,rmenor):
        if menor[x] == maior[i]:
            c.append(maior[i])
print(c)
            
