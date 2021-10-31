import keyboard
import time

inputKey = input("Introduzca que quieres spamear: ") 
while True:
    if keyboard.on_press('alt'):
        while True:
            keyboard.write(inputKey)
            time.sleep(0.01)
            keyboard.send('enter')
            time.sleep(0.01)
    if keyboard.is_pressed('esc'):
        break  