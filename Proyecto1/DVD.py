import arcade
from arcade import color
from random import randint

def draw(deltaTime):
    global posX, posY, movX, movY, size, colour1, colour2, colour3

    arcade.start_render()
    arcade.set_background_color(color.AIR_FORCE_BLUE)

    arcade.draw_rectangle_filled(posX,posY,size,size,(colour1,colour2,colour3))

    posX += movX
    posY += movY

    if posX >= windW-size/2 or posX <= size/2:
        movX *= -1
        colour1 = randint(0,255)
        colour2 = randint(0,255)
        colour2 = randint(0,255)
    if posY >= windH-size/2 or posY <= size/2:
        movY *= -1 
        colour1 = randint(0,255)
        colour2 = randint(0,255)
        colour2 = randint(0,255)
windW = 800
windH = 600

posX = windW/2
posY = windH/2
movX = 5
movY = 5
size = 100
colour1 = 255
colour2 = 255
colour3 = 255

arcade.open_window(windW,windH, "DVD")

arcade.schedule(draw,1/60)

arcade.run()