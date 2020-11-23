a = 1988777790
b = 2890


def igualdadedois(a,b):
    if a%100 == b%100:
        return True
    else:
        return False
print(igualdadedois(a,b))