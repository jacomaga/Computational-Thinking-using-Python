a = [2,4,5,1,3,6,8,9,10]
b = []
for i in range(0,len(a)):
    if a[i] % 2 == 0:
        b.append(a[i])
print(b)
