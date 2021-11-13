import arcade
from arcade import color
from random import randint

def draw(deltaTime):
    global posX

    arcade.start_render()
    arcade.set_background_color(color.AIR_FORCE_BLUE)

    arcade.draw_rectangle_filled(posX,posY,size,size,color.RED)

    posX += 100 * deltaTime

    arcade.finish_render

windW = 800
windH = 600

posX = 0
posY = windH/2
movX = 5
movY = 5
size = 50

arcade.open_window(windW,windH, "DVD")

arcade.schedule(draw,1/144)
arcade.run()