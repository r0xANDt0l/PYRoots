import random

minN = int(input("Dime el primer numero: "))
maxN = int(input("Dime el segundo numero: "))
atts = 0

N = int(input("Dime el numero que intentas buscar: "))

while N >= minN and N <= maxN:
    rnd = random.randint(minN, maxN)
    if N == rnd:
        print("Encontrado, me ha llevado esta cantidad de intentos: ")
        print(atts)
        break
    else:
        atts += 1


# Shortcut test ctrl + shift + Z
