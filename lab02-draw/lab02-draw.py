import arcade
from arcade import finish_render
from arcade.color import YELLOW

arcade.open_window(800, 600, "Un dibujinho")
arcade.set_background_color(arcade.color.ELECTRIC_CYAN)
arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 800, 100, 0, arcade.color.BLUE_GREEN)

#mar
arcade.draw_arc_filled(206, 115, 150, 60, arcade.color.ELECTRIC_CYAN, 180, 360)
arcade.draw_arc_filled(475, 115, 150, 60, arcade.color.ELECTRIC_CYAN, 180, 360)
arcade.draw_arc_filled(745, 115, 150, 60, arcade.color.ELECTRIC_CYAN, 180, 360)
arcade.draw_ellipse_filled(70, 90, 150, 60,arcade.color.BLUE_GREEN)
arcade.draw_ellipse_filled(341, 90, 150, 60,arcade.color.BLUE_GREEN)
arcade.draw_ellipse_filled(610, 90, 150, 60,arcade.color.BLUE_GREEN)
#barco
arcade.draw_arc_filled(470, 150, 350, 120, arcade.color.WOOD_BROWN, 178, 360,358)
arcade.draw_lrtb_rectangle_filled(350, 600, 100, 0, arcade.color.BLUE_GREEN)
arcade.draw_rectangle_filled(410, 250, 10, 250,arcade.color.WOOD_BROWN,2)
arcade.draw_rectangle_filled(520, 210, 10, 210,arcade.color.WOOD_BROWN,2)
arcade.draw_triangle_filled(528, 310, 526, 200, 600, 198, arcade.color.WHITE_SMOKE)
arcade.draw_triangle_filled(418, 370, 416, 275, 480, 273, arcade.color.WHITE_SMOKE)
arcade.draw_triangle_filled(415, 260, 413, 170, 478, 168, arcade.color.WHITE_SMOKE)
arcade.draw_arc_filled(528, 260, 20, 100, arcade.color.WHITE, 270, 450,358)
arcade.draw_arc_filled(418, 320, 20, 100, arcade.color.WHITE, 270, 450,358)
arcade.draw_arc_filled(415, 210, 20, 100, arcade.color.WHITE, 270, 450,358)
#sol
arcade.draw_circle_filled(100,500,40,arcade.color.YELLOW)
#burbujas

arcade.draw_circle_outline(150, 50, 7, arcade.color.LIGHT_BLUE)
arcade.draw_circle_outline(145, 30, 5, arcade.color.LIGHT_BLUE)
arcade.draw_circle_outline(155, 20, 5, arcade.color.LIGHT_BLUE)
arcade.draw_circle_outline(460, 45, 5, arcade.color.LIGHT_BLUE)
arcade.draw_circle_outline(450, 25, 4, arcade.color.LIGHT_BLUE)
arcade.draw_circle_outline(700, 60, 6, arcade.color.LIGHT_BLUE)
arcade.draw_circle_outline(705, 30, 6, arcade.color.LIGHT_BLUE)
arcade.draw_circle_outline(720, 15, 5, arcade.color.LIGHT_BLUE)
#barco

arcade,finish_render()
arcade.run()