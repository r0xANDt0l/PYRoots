import numbers
import arcade
import math
import keyword
from arcade import color
from random import randint


windW = 800
windH = 600


numbS = 1
speed = 5

img = arcade.Sprite("Fotos/doge.png")


def RNDColor():
    return(randint(0,255) ,randint(0,255) ,randint(0,255) )

def draw(deltaTime):

    arcade.start_render()

    for i in range(numbS):
        # arcade.draw_circle_filled(posX[i],posY[i],radius,colour[i])


        posX[i] += movX[i]
        posY[i] += movY[i]
        img.draw()
        img.set_position(posX[i],posY[i])

        if posX[i] >= windW-img.width or posX[i] <= img.width:
            movX[i] *= -1
            posX[i] += movX[i]
            colour[i] = RNDColor()
        if posY[i] >= windH-img.height or posY[i] <= img.height:
            movY[i] *= -1 
            posY[i] += movY[i]
            colour[i] = RNDColor()
       
posX = [randint(img.width,windW-img.width) for i in range(numbS)]
posY = [randint(img.height,windH-img.height) for i in range(numbS)]

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