import arcade
from arcade import color
from random import randint

def draw(deltaTime):
    global posX, posY, movX, movY, size, colour

    arcade.start_render()
    arcade.set_background_color(color.AIR_FORCE_BLUE)

    arcade.draw_rectangle_filled(posX,posY,size,size,(colour,colour,colour))

    posX += movX
    posY += movY

    if posX >= windW-size/2 or posX <= 0+size/2:
        movX *= -1
        colour = randint(0,255)
    if posY >= windH-size/2 or posY <= 0+size/2:
        movY *= -1 
        colour = randint(0,255)
    

windW = 800
windH = 600

posX = windW/2
posY = windH/2
movX = 2
movY = 2
size = 50
colour = 255

arcade.open_window(windW,windH, "DVD")

arcade.schedule(draw,1/60)

arcade.run()