import numbers
import arcade
from arcade import color
from random import randint


def RNDColor():
    return(randint(0,255) ,randint(0,255) ,randint(0,255) )

def draw(deltaTime):
    
    arcade.start_render()

    for i in range(numbS):
        arcade.set_background_color(color.AIR_FORCE_BLUE)

        arcade.draw_circle_filled(posX[i],posY[i],size,colour[i])

        posX[i] += movX[i]
        posY[i] += movY[i]

        if posX[i] >= windW-size or posX[i] <= size:
            movX[i] *= -1
            colour[i] = RNDColor()
        if posY[i] >= windH-size or posY[i] <= size:
            movY[i] *= -1 
            colour[i] = RNDColor()
windW = 800
windH = 600


size = 25
numbS = randint(1,25)
posX = [randint(size,windW-size) for i in range(numbS)]
posY = [randint(size,windW-size) for i in range(numbS)]

movX = [randint(-10,10) for i in range(numbS)]
movY = [randint(-10,10) for i in range(numbS)]
colour = [RNDColor() for i in range(numbS)]

arcade.open_window(windW,windH, "DVD")

arcade.schedule(draw,1/60)

arcade.run()