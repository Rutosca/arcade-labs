import arcade

from arcade import MOUSE_BUTTON_LEFT
from arcade import MOUSE_BUTTON_RIGHT
from random import *
import time
import os

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
class Rectangle:
    def __init__(self,rect_x,rect_y,rect_width,rect_height,color):
        self.rect_x=rect_x
        self.rect_y=rect_y
        self.rect_width=rect_width
        self.rect_height=rect_height
        self.color=color
    def draw(self):
        arcade.draw_rectangle_filled(self.rect_x, self.rect_y, self.rect_width, self.rect_height, self.color)
class Out_line:
    def __init__(self,line_x,line_y,line_width,line_height,line_color,line_g):
        self.line_x=line_x
        self.line_y=line_y
        self.line_width=line_width
        self.line_height=line_height
        self.line_color=line_color
        self.line_g=line_g
    def draw(self):
        arcade.draw_rectangle_outline(self.line_x, self.line_y, self.line_width, self.line_height, self.line_color,self.line_g)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.color_transparente = (0, 200, 100, 150)
        arcade.set_background_color(arcade.color.ENGLISH_GREEN)

        self.rect_list=[]
        self.outline=[]

        rect=Rectangle(500,350,200,200,self.color_transparente)
        self.rect_list.append(rect)
        out=Out_line(500, 350, 200, 200, arcade.color.BLACK, 5)
        self.outline.append(out)

        rect = Rectangle(700, 300, 200, 100, self.color_transparente)
        self.rect_list.append(rect)
        out = Out_line(700, 300, 200, 100, arcade.color.BLACK, 5)
        self.outline.append(out)

        rect = Rectangle(300, 300, 200, 100, self.color_transparente)
        self.rect_list.append(rect)
        out = Out_line(300, 300, 200, 100, arcade.color.BLACK, 5)
        self.outline.append(out)

        rect = Rectangle(300, 400, 200, 100, self.color_transparente)
        self.rect_list.append(rect)
        out = Out_line(300, 400, 200, 100, arcade.color.BLACK, 5)
        self.outline.append(out)

        rect = Rectangle(700, 400, 200, 100, self.color_transparente)
        self.rect_list.append(rect)
        out = Out_line(700, 400, 200, 100, arcade.color.BLACK, 5)
        self.outline.append(out)
        #jugador
        self.eleccion_jug = None
        self.posicion_jug = None
        self.gol_jug = 0
        self.turno_jug=True
        # bot
        self.eleccion_IA = None
        self.posicion_IA = None
        self.gol_IA = 0
        self.turno_IA=False
        # ronda y numero límite de rondas
        self.ronda = 1
        self.final = 5
        self.dibujar_rectangulo=True
        self.mensaje="Choose your shot"
        self.portada=True



    def on_draw(self):
        self.clear()
        # Dibujar el área en la que queremos detectar clics (ejemplo: un rectángulo)
        if self.dibujar_rectangulo:
            for rect in self.rect_list:
                rect.draw()
            for out in self.outline:
                out.draw()
        # Dibujar marcador

        arcade.draw_text(f"Ronda: {self.ronda}", 50, SCREEN_HEIGHT - 50, arcade.color.WHITE, 20)
        arcade.draw_text(f"Jugador: {self.gol_jug} - IA: {self.gol_IA}", 50, SCREEN_HEIGHT - 80,
                         arcade.color.WHITE, 20)

        arcade.draw_text(self.mensaje, 400, 500, arcade.color.CYAN, 20)




    def bot_action_keeper(self,delta_time):
        self.mensaje="Choose your shot"

        self.eleccion_IA = 0
        self.posicion_IA = 0
        print(f"Turno de IA: Parar...")

        self.eleccion_IA = randint(1, 3)

        if self.eleccion_IA == 1 or self.eleccion_IA == 3:
            self.posicion_IA = randint(1, 2)
        else:
            self.posicion_IA=None

        self.turno_IA=True
        arcade.unschedule(self.bot_action_keeper)
        arcade.schedule(self.comprobar_acciones_tiro, 2)
        arcade.schedule(self.bot_action_shoot, 4)

    def bot_action_shoot(self,delta_time):
        self.mensaje="Choose your move"
        self.eleccion_IA = 0
        self.posicion_IA = 0
        print(f"Turno de IA: Tirar...")

        self.eleccion_IA = randint(1, 3)

        if self.eleccion_IA == 1 or self.eleccion_IA == 3:
            self.posicion_IA = randint(1, 2)
        else:
            self.posicion_IA = None
        arcade.unschedule(self.bot_action_shoot)
        self.turno_jug=True
        self.dibujar_rectangulo=True
        self.turno_IA=False






    def on_mouse_press(self, x, y, button, modifiers):

        if self.turno_jug:
            #Definir los límites del área de detección (rectángulo en este caso)
            rect_x1,rect_y1,rect_width1,rect_height1= 500,350,200,200
            rect_x2, rect_y2, rect_width2, rect_height2 = 700, 300, 200, 100
            rect_x3, rect_y3, rect_width3, rect_height3 = 300, 300, 200, 100
            rect_x4, rect_y4, rect_width4, rect_height4 = 300, 400, 200, 100
            rect_x5, rect_y5, rect_width5, rect_height5 = 700, 400, 200, 100

            # Verificar si el clic ocurrió dentro del rectángulo
            if (rect_x1 - rect_width1 / 2) <= x <= (rect_x1 + rect_width1 / 2) and \
               (rect_y1 - rect_height1 / 2) <= y <= (rect_y1 + rect_height1 / 2) :
                self.eleccion_jug=2
                self.posicion_jug=None
                self.dibujar_rectangulo = False
                self.turno_jug = False


            elif (rect_x2 - rect_width2 / 2) <= x <= (rect_x2 + rect_width2 / 2) and \
                 (rect_y2 - rect_height2 / 2) <= y <= (rect_y2 + rect_height2 / 2) :
                self.eleccion_jug = 3
                self.posicion_jug=2
                self.dibujar_rectangulo = False
                self.turno_jug = False


            elif (rect_x3 - rect_width3 / 2) <= x <= (rect_x3 + rect_width3 / 2) and \
                 (rect_y3 - rect_height3 / 2) <= y <= (rect_y3 + rect_height3 / 2) :
                self.eleccion_jug = 1
                self.posicion_jug=2
                self.dibujar_rectangulo = False
                self.turno_jug = False


            elif (rect_x4 - rect_width4 / 2) <= x <= (rect_x4 + rect_width4 / 2) and \
                 (rect_y4 - rect_height4 / 2) <= y <= (rect_y4 + rect_height4 / 2) :
                self.eleccion_jug = 1
                self.posicion_jug=1
                self.dibujar_rectangulo = False
                self.turno_jug = False


            elif (rect_x5 - rect_width5 / 2) <= x <= (rect_x5 + rect_width5 / 2) and \
                 (rect_y5 - rect_height5 / 2) <= y <= (rect_y5 + rect_height5 / 2):
                self.eleccion_jug = 3
                self.posicion_jug = 1
                self.dibujar_rectangulo = False
                self.turno_jug=False

#comprobaciones

        elif not self.turno_jug:
            return

        if not self.turno_IA:
            arcade.schedule(self.bot_action_keeper,1)




        print(self.eleccion_jug,self.posicion_jug)



    def comprobar_acciones_tiro(self,delta_time):
        """Para comprobar tiros del jugador"""
        # no coincide:gol
        if self.eleccion_jug != self.eleccion_IA:

            print("Gol")
            self.gol_jug += 1

        # coincide:comprobar
        # primer caso:izquierda tira jugador
        elif self.eleccion_jug == 1 and self.eleccion_IA == 1:

            if self.posicion_jug == self.posicion_IA:

                print("Parada")

            else:

                print("Gol")
                self.gol_jug += 1

        # segundo caso:centro tira jugador
        elif self.eleccion_jug == 2 and self.eleccion_IA == 2:

            print("Parada");

        # tercer caso:derecha tira jugador
        elif self.eleccion_jug == 3 and self.eleccion_IA == 3:

            if self.posicion_jug == self.posicion_IA:

                print("Parada")

            else:

                print("Gol")
                self.gol_jug += 1

        arcade.unschedule(self.comprobar_acciones_tiro)

    def comprobar_acciones_parada(self,delta_time):
        """Para comprobar paradas del jugador"""
        # no coincide:gol
        if self.eleccion_jug != self.eleccion_IA:

            print("Gol")
            self.gol_IA += 1


        # coincide:comprobar
        # primer caso:izquierda tira jugador
        elif self.eleccion_jug == 1 and self.eleccion_IA == 1:

            if self.posicion_jug == self.posicion_IA:

                print("Parada")

            else:

                print("Gol")
                self.gol_IA += 1


        # segundo caso:centro tira jugador
        elif self.eleccion_jug == 2 and self.eleccion_IA == 2:

            print("Parada");

        # tercer caso:derecha tira jugador
        elif self.eleccion_jug == 3 and self.eleccion_IA == 3:

            if self.posicion_jug == self.posicion_IA:

                print("Parada")

            else:

                print("Gol")
                self.gol_jug += 1

        arcade.unschedule(self.comprobar_acciones_tiro)






def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Penalti inazuma eleven")
    arcade.run()

main()




