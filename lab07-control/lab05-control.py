import arcade
import pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

# Inicializamos Pygame y su subsistema de joystick.
pygame.init()
pygame.joystick.init()
joystick = None
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Joystick detectado: {joystick.get_name()}")
else:
    print("No se detectaron joysticks.")

class Plane:
    def __init__(self, position_x, position_y,color):
        # La posición del avión se define como el centro del fuselaje.
        self.position_x = position_x
        self.position_y = position_y
        self.color=color

    def draw(self):
        # Se define el centro original del dibujo (centro del fuselaje) para reajustarlo.
        center_x = 150
        center_y = 100
        xp = self.position_x
        yp = self.position_y

        # Ala principal (se reubica restando el centro)
        arcade.draw_polygon_filled([
            (150 + xp - center_x, 105 + yp - center_y),
            (130 + xp - center_x, 130 + yp - center_y),
            (170 + xp - center_x, 105 + yp - center_y)
        ], arcade.color.DARK_GRAY)

        # Fuselaje (elipse), centrado en (xp, yp)
        arcade.draw_ellipse_filled(150 + xp - center_x, 100 + yp - center_y, 100, 25, arcade.color.LIGHT_GRAY)
        # Cabina
        arcade.draw_ellipse_filled(180 + xp - center_x, 105 + yp - center_y, 20, 10, arcade.color.LIGHT_BLUE)
        # Nariz
        arcade.draw_triangle_filled(210 + xp - center_x, 100 + yp - center_y,
                                      190 + xp - center_x, 107 + yp - center_y,
                                      190 + xp - center_x, 92 + yp - center_y,
                                      arcade.color.LIGHT_GRAY)
        # Alerón vertical (cola)
        arcade.draw_triangle_filled(150 + xp - center_x, 100 + yp - center_y,
                                      90 + xp - center_x, 120 + yp - center_y,
                                      100 + xp - center_x, 100 + yp - center_y,
                                      arcade.color.LIGHT_GRAY)
        # Alerón horizontal (estabilizador trasero)
        arcade.draw_triangle_filled(110 + xp - center_x, 100 + yp - center_y,
                                      105 + xp - center_x, 95 + yp - center_y,
                                      105 + xp - center_x, 105 + yp - center_y,
                                      arcade.color.LIGHT_GRAY)
        # Otra ala, inferior
        arcade.draw_polygon_filled([
            (142 + xp - center_x, 100 + yp - center_y),
            (110 + xp - center_x, 80 + yp - center_y),
            (160 + xp - center_x, 100 + yp - center_y)
        ], arcade.color.DARK_GRAY)



class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        # Ocultamos el puntero del ratón.
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.ELECTRIC_BLUE)
        # Inicializamos el avión en el centro de la ventana.
        self.plane = Plane(width // 2, height // 2, arcade.color.GOLD)


    def on_draw(self):
        self.clear()
        self.plane.draw()
        # Indicador visual de si se detectó el joystick.
        if joystick:
            arcade.draw_text("Joystick activo", 10, SCREEN_HEIGHT - 30, arcade.color.GREEN, 20)
        else:
            arcade.draw_text("Sin joystick", 10, SCREEN_HEIGHT - 30, arcade.color.RED, 20)

    def on_mouse_motion(self, x, y, dx, dy):
        # Permite mover el avión con el ratón si se desea (aunque se puede comentar si se quiere solo joystick).
        self.plane.position_x = x
        self.plane.position_y = y


    def on_update(self, delta_time):
        # eventos de Pygame para actualizar el estado del joystick.
        pygame.event.pump()
        if joystick:
            # Se leen los ejes del joystick.
            x_axis = joystick.get_axis(0)
            y_axis = joystick.get_axis(1)
            plane_speed = 1000  # Velocidad en píxeles por segundo.
            # Actualizamos la posición del avión.
            self.plane.position_x += x_axis * plane_speed * delta_time
            # Normalmente el eje Y está invertido, así que usamos -y_axis.
            self.plane.position_y += -y_axis * plane_speed * delta_time

            while self.plane.position_x<-200:
                self.plane.position_x=1200
            while self.plane.position_x>1200:
                self.plane.position_x=-200
            while self.plane.position_y < -100:
                self.plane.position_y = 800
            while self.plane.position_y > 800:
                self.plane.position_y = -100

    def get_bounding_box(self):
        width = 100  # Aproximado al tamaño del fuselaje
        height = 25  # Aproximado al fuselaje
        return (self.position_x - width // 2, self.position_y - height // 2,
                self.position_x + width // 2, self.position_y + height // 2)


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Avión controlado con Joystick (Pygame + Arcade)")
    arcade.run()

if __name__ == "__main__":
    main()
