import arcade
from arcade import color
from random import randint

def draw(deltaTime):
    arcade.start_render()
    arcade.set_background_color(color.AIR_FORCE_BLUE)

    arcade.draw_rectangle_filled(randint(0,windW),posY,size,size,color.RED)

    arcade.finish_render

windW = 800
windH = 600

posX = windW/2
posY = windH/2
movX = 5
movY = 5
size = 50

arcade.open_window(windW,windH, "DVD")

arcade.schedule()
arcade.run()