import numbers
import arcade
import math
import keyword
from arcade import color
from random import randint
from random import uniform

windW = 1240
windH = 720

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

    movX[i] += gravX[i]
    movY[i] += gravY[i]
    movX[i] *= friction
    movY[i] *= friction

def draw(deltaTime):
    global t, gravX, gravY
    arcade.start_render()
    
    t -=deltaTime

    # round(t,2)
    if t <= 0:
        t = 5
        gravX = [randint(-5,5) for i in range(numbS)]
        gravY = [randint(-5,5) for i in range(numbS)]


    
    arcade.draw_text("%.2f"%t,windW/2,windH/1.5,color.WHITE,50)

    for i in range(numbS):
        gravXLine = gravX[i]*20+posX[i]
        gravYLine = gravY[i]*20+posY[i]
        dirXLine = movX[i]
        dirYLine = movY[i]
        mod = math.sqrt(dirXLine**2 + dirYLine**2)
        dirXLine /=mod if mod != 0 else 1
        dirYLine /=mod if mod != 0 else 1
        dirXLine *= radius
        dirYLine *= radius
        arcade.draw_circle_filled(posX[i],posY[i],radius,colour[i])

        arcade.draw_line(posX[i],posY[i],gravXLine,gravYLine,color=color.RED)
        arcade.draw_line(posX[i],posY[i],dirXLine+posX[i],dirYLine+posY[i],color=color.GREEN)

        movement(i)

        for j in range(numbS):
            if i == j:
                continue
            # CheckCollision(i,j)

       


radius = 25
numbS = 5
t = 5

gravX = [0 for i in range(numbS)]
gravY = [0 for i in range(numbS)]

friction = 0.03
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