import random
import time

minN = int(input("Dime el primer numero: "))
maxN = int(input("Dime el segundo numero: "))
atts = 1

N = int(input("Dime el numero que intentas buscar: "))
TimeStr = time.time()

while N >= minN and N <= maxN:
    rnd = random.randint(minN, maxN)
    if N == rnd:
        TimeEnd = time.time()
        TimeTok = TimeEnd - TimeStr
        print("Encontrado, me ha llevado ", atts,
              " intentos y me ha llevado ", TimeTok, "seg")
        break
    else:
        atts += 1


# Shortcut test ctrl + shift + Z
# Didn't work :(
