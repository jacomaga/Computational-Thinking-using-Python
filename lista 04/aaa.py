n = 12345678911
c = (n%10**8)
#123.456.789-10
d = c%10**5 
e = d%10**2
print(n%10**2)
print((d-e)//100)
print((c-d)//100000)
print((n-c)//100000000)
#https://www.youtube.com/watch?v=B3F0IjH5WAM