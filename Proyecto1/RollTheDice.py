import keyboard #Importar la libreria de cosas de teclado
import random #Importar la libreria de cosas random
import time

sides = 1
sidesSelect = input("Amount of sides the dice has. If empty, 6: ")
is_non_empty= bool(sidesSelect)
if is_non_empty is False:
    sides = 6
else:
    sides = sidesSelect

time.sleep(0.5)

while True: #Un loop
    nmb = random.randint(1,sides) #Obtener numero al azar
    print("The dice rolled ", nmb) #Decir el numero que ha tocado
    input('Press enter to roll the dice again') #Decir si quiere tirar de nuevo
    time.sleep(random.uniform(0.2,0.8))