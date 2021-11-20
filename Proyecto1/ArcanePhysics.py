import numbers
import arcade
import math
import keyword
from arcade import color
from random import randint


def RNDColor():
    return(randint(0,255) ,randint(0,255) ,randint(0,255) )

def CheckCollision(i : int, j : int):
    if i == j:  
        return
        
    x = posX[j]-posX[i]
    y = posY[j]-posY[i]

    mod = math.sqrt( x*x + y*y )
    if mod <= radius*2:
        x /= mod
        y /= mod
        x *=speed
        y *= speed
        movX[i] = -x
        movY[i] = -y
        movX[j] = x
        movY[j] = y
        colour[i] = RNDColor()



def movement( i : int):
    posX[i] += movX[i]
    posY[i] += movY[i]

    if posX[i] >= windW-radius or posX[i] <= radius:
        movX[i] *= -1
        posX[i] += movX[i]
        movX[i] *= elas
        # colour[i] = RNDColor()
    if posY[i] >= windH-radius or posY[i] <= radius:
        movY[i] *= -1 
        posY[i] += movY[i]
        movY[i] *= elas
        # colour[i] = RNDColor()

    movX[i] += gravX
    movY[i] += gravY
    # movX[i] *= 0.97
    # movY[i] *= 0.97

def draw(deltaTime):
    
    arcade.start_render()

    for i in range(numbS):
        arcade.draw_circle_filled(posX[i],posY[i],radius,colour[i])

        movement(i)

        for j in range(numbS):
            if i == j:
                continue
            CheckCollision(i,j)

       
windW = 800
windH = 600


radius = 25
numbS = 14

gravX = 0
gravY = -1
elas = -0.8

speed = randint(1,20)
posX = [randint(radius,windW-radius) for i in range(numbS)]
posY = [randint(radius,windH-radius) for i in range(numbS)]

movX = [randint(-10,10) for i in range(numbS)]
movY = [randint(-10,10) for i in range(numbS)]



colour = [RNDColor() for i in range(numbS)]

arcade.open_window(windW,windH, "DVD")

arcade.schedule(draw,1/60)

arcade.run()