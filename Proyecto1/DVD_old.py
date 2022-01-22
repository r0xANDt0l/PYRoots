import numbers
import arcade
import math
import keyword
from arcade import color
from random import randint


def RNDColor():
    return(randint(0,255) ,randint(0,255) ,randint(0,255) )

def movement( i : int):
    posX[i] += movX[i]
    posY[i] += movY[i]

    if posX[i] >= windW-radius or posX[i] <= radius:
        movX[i] *= -1
        posX[i] += movX[i]
        colour[i] = RNDColor()
    if posY[i] >= windH-radius or posY[i] <= radius:
        movY[i] *= -1 
        posY[i] += movY[i]
        colour[i] = RNDColor()

def draw(deltaTime):

    arcade.start_render()

    for i in range(numbS):
        arcade.draw_circle_filled(posX[i],posY[i],radius,colour[i])

        movement(i)
       
windW = 800
windH = 600


radius = 50
numbS = 1
speed = 5
posX = [randint(radius,windW-radius) for i in range(numbS)]
posY = [randint(radius,windH-radius) for i in range(numbS)]

movX = [45]
movY = [45]

for i in range(numbS):
    x = movX[i]
    y = movY[i]
    mod = math.sqrt(x*x+y*y)

    x/= mod
    y/= mod

    x *= speed
    y *= speed

    movX[i] = x
    movY[i] = y


colour = [RNDColor() for i in range(numbS)]

arcade.open_window(windW,windH, "DVD")

arcade.schedule(draw,1/120)

arcade.run()