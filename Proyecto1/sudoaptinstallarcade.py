import arcade
from arcade import color
import random
width = 800
height = 600

def StopSign(X,Y,SizeOfCircle):
    arcade.draw_rectangle_filled(random.uniform(X*0.90,X*1.19), Y/2, SizeOfCircle/10, SizeOfCircle*3, color.BRONZE)
    arcade.draw_circle_filled(X, Y ,SizeOfCircle, color.RED_DEVIL)
    arcade.draw_rectangle_filled(X, Y, SizeOfCircle*1.5, SizeOfCircle/2.5, color.BABY_POWDER)


arcade.open_window(width,height, "Ventanilla de los")

arcade.set_background_color(color.BABY_POWDER)

arcade.start_render()

StopSign(width/4, height/4, 100)
StopSign(width/2, height/2, 100)

arcade.finish_render()

arcade.run()
