import arcade
from arcade import color

arcade.open_window(800,600, "Mi ventana!!!!!!!!!!!!!111 hols")

arcade.set_background_color(color.BLACK_LEATHER_JACKET)

arcade.start_render()

arcade.draw_circle_filled(400,300,200,color.RED)

arcade.finish_render()

arcade.run()
