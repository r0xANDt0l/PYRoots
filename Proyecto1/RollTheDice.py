import keyboard #Importar la libreria de cosas de teclado
import random #Importar la libreria de cosas random

input('Press enter to roll the dice') #Pedir pulsar el enter para empezar
while True: #Un loop
    nmb = random.randint(1,6) #Obtener numero al azar
    print("The dice rolled ", nmb) #Decir el numero que ha tocado
    input('Press enter to roll the dice again') #Decir si quiere tirar de nuevo