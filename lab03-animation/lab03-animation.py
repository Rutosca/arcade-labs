import arcade
import math
from arcade import finish_render
from arcade.color import YELLOW

def draw_sea():
    """Function to draw the sea"""
    arcade.draw_lrtb_rectangle_filled(0, 800, 100, 0, arcade.color.BLUE_GREEN)
    arcade.draw_arc_filled(206, 115, 150, 60, arcade.color.ELECTRIC_CYAN, 180, 360)
    arcade.draw_arc_filled(475, 115, 150, 60, arcade.color.ELECTRIC_CYAN, 180, 360)
    arcade.draw_arc_filled(745, 115, 150, 60, arcade.color.ELECTRIC_CYAN, 180, 360)
    arcade.draw_ellipse_filled(70, 90, 150, 60,arcade.color.BLUE_GREEN)
    arcade.draw_ellipse_filled(341, 90, 150, 60,arcade.color.BLUE_GREEN)
    arcade.draw_ellipse_filled(610, 90, 150, 60,arcade.color.BLUE_GREEN)
def draw_sailboat(angle,x):
    """Function to draw the sailboat """
    arcade.draw_arc_filled(x+470, 150, 350, 120, arcade.color.WOOD_BROWN, 178, 360,angle+356)
    arcade.draw_rectangle_filled(400, 50, 800, 100, arcade.color.BLUE_GREEN) #A "piece" of Sea
    arcade.draw_rectangle_filled(x+410, 250, 10, 250,arcade.color.WOOD_BROWN,-angle)
    arcade.draw_rectangle_filled(x+520, 210, 10, 210,arcade.color.WOOD_BROWN,-angle)
    arcade.draw_triangle_filled(x+528-angle, 310, x+526-angle, 200, x+600-angle, 198, arcade.color.WHITE_SMOKE)
    arcade.draw_triangle_filled(x+418-angle, 370, x+416-angle, 275, x+480-angle, 273, arcade.color.WHITE_SMOKE)
    arcade.draw_triangle_filled(x+415-angle, 260, x+413-angle, 170, x+478-angle, 168, arcade.color.WHITE_SMOKE)
    arcade.draw_arc_filled(x+524-angle, 260, 20, 100, arcade.color.WHITE, 270, 450,362+angle)
    arcade.draw_arc_filled(x+415-angle, 320, 20, 100, arcade.color.WHITE, 270, 450,362+angle)
    arcade.draw_arc_filled(x+415+angle, 210, 20, 100, arcade.color.WHITE, 270, 450,362+angle)
def draw_sun():

    arcade.draw_circle_filled(100,500,40,arcade.color.YELLOW)

def draw_bubbles(angle):
    arcade.draw_circle_outline(150+angle, 50, 7, arcade.color.LIGHT_BLUE)
    arcade.draw_circle_outline(145-angle, 30, 5, arcade.color.LIGHT_BLUE)
    arcade.draw_circle_outline(155+angle, 20, 5, arcade.color.LIGHT_BLUE)
    arcade.draw_circle_outline(460-angle, 45, 5, arcade.color.LIGHT_BLUE)
    arcade.draw_circle_outline(450+angle, 25, 4, arcade.color.LIGHT_BLUE)
    arcade.draw_circle_outline(700-angle, 60, 6, arcade.color.LIGHT_BLUE)
    arcade.draw_circle_outline(705+angle, 30, 6, arcade.color.LIGHT_BLUE)
    arcade.draw_circle_outline(720-angle, 15, 5, arcade.color.LIGHT_BLUE)

def on_draw(delta_time):
    """Draws everything"""
    on_draw.angle=on_draw.A*math.sin(on_draw.v*on_draw.t)
    arcade.start_render()
    draw_sea()
    draw_sailboat(on_draw.angle,on_draw.x)
    draw_sun()
    draw_bubbles(on_draw.angle)
    on_draw.t+=1
    on_draw.x+=1

on_draw.x=0

on_draw.A=3
on_draw.v=0.03
on_draw.t=0

def main():

    arcade.open_window(800, 600, "Un dibujinho con funciones")
    arcade.set_background_color(arcade.color.ELECTRIC_CYAN)

    arcade.schedule(on_draw, 1/60)
    arcade.run()

main()