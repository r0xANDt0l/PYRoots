import numbers
import arcade
import math
import keyword
from arcade import color
from random import randint
from random import uniform


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
    movX[i] *= friction
    movY[i] *= friction

def draw(deltaTime):
    global t
    arcade.start_render()
    
    t -=deltaTime

    round(t,2)

    if t <= 0:
        t = 5
        # numbS += 1
    arcade.draw_text(str(t),windW/2,windH/3)

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
numbS = 1
t = 5

gravX = 0
gravY = -1

friction = uniform(0.9,0.999)
elas = 1

speed = randint(1,20)
posX = [randint(radius,windW-radius) for i in range(numbS)]
posY = [randint(radius,windH-radius) for i in range(numbS)]

movX = [randint(-10,10) for i in range(numbS)]
movY = [randint(-10,10) for i in range(numbS)]



colour = [RNDColor() for i in range(numbS)]

arcade.open_window(windW,windH, "Grav sim")

arcade.schedule(draw,1/60)

arcade.run()