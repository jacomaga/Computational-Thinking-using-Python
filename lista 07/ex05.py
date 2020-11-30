strings = ("lalala","lalalala","lalalalala")
maior = 0
for i in strings:
    if len(i) > maior:
        maior = len(i)
print(maior)
