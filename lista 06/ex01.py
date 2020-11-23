a =input("Digite algo sem acento:")
a = list(a)
b =""
arange = len(a)-1
i = 0
def myUppercase(a):
    while i < len(a):
        if a[i] == 'a':
            a[i] = "A"
        if a[i] == 'b':
            a[i] = "B"
        if a[i] == 'c':
            a[i] = "C"
        if a[i] == 'd':
            a[i] = "D"
        if a[i] == 'e':
            a[i] = "E"
        if a[i] == 'f':
            a[i] = "F"
        if a[i] == 'g':
            a[i] = "G"
        if a[i] == 'h':
            a[i] = "H"
        if a[i] == 'i':
            a[i] = "I"
        if a[i] == 'j':
            a[i] = "J"
        if a[i] == 'k':
            a[i] = "K"
        if a[i] == 'l':
            a[i] = "L"
        if a[i] == 'm':
            a[i] = "M"
        if a[i] == 'o':
            a[i] = "O"          
        if a[i] == 'p':
            a[i] = "P"  
        if a[i] == 'q':
            a[i] = "Q"  
        if a[i] == 'r':
            a[i] = "R"  
        if a[i] == 's':
            a[i] = "S"  
        if a[i] == 't':
            a[i] = "T"
        if a[i] == 'u':
            a[i] = "U"  
        if a[i] == 'v':
            a[i] = "V"  
        if a[i] == 'w':
            a[i] = "W"  
        if a[i] == 'y':
            a[i] = "Y"
        if a[i] == 'z':
            a[i] = "Z"          
            
        i+=1
    return a
print(myUppercase(a))
# -*- coding: utf-8 -*-
a =input("Digite algo:")
a = a.upper()
print(a)
