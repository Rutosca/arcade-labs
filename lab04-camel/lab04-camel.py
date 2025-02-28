import arcade
from arcade import MOUSE_BUTTON_LEFT

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

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BUD_GREEN)
        self.rect_list=[]
        rect=Rectangle(400,300,200,100,arcade.color.YELLOW)
        self.rect_list.append(rect)
        rect = Rectangle(500, 400, 300, 200, arcade.color.YELLOW)
        self.rect_list.append(rect)
        rect = Rectangle(100, 50, 100, 50, arcade.color.YELLOW)
        self.rect_list.append(rect)
        rect = Rectangle(400, 300, 200, 100, arcade.color.YELLOW)
        self.rect_list.append(rect)
        rect = Rectangle(400, 300, 200, 100, arcade.color.YELLOW)
        self.rect_list.append(rect)


    def on_draw(self):
        self.clear()
        # Dibujar el área en la que queremos detectar clics (ejemplo: un rectángulo)
        for rect in self.rect_list:
            rect.draw()


    def on_mouse_press(self, x, y, button, modifiers):
        # Definir los límites del área de detección (rectángulo en este caso)
        rect_x1 = 500  # Centro del rectángulo
        rect_y1 = 350
        rect_width1 = 200
        rect_height1 = 100

        # Verificar si el clic ocurrió dentro del rectángulo
        if (rect_x1 - rect_width1 / 2) <= x <= (rect_x1 + rect_width1 / 2) and \
           (rect_y1 - rect_height1 / 2) <= y <= (rect_y1 + rect_height1 / 2):
            print("¡Clic dentro del área!")
            print(" ")

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Detección de clics")
    arcade.run()

main()
