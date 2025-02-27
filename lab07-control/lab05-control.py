import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

class Plane:
    def __init__(self, position_x, position_y):
        # La posición del avión se define como el centro del fuselaje.
        self.position_x = position_x
        self.position_y = position_y

    def draw(self):
        # Se define el centro original del dibujo (centro del fuselaje) para reajustarlo
        center_x = 300
        center_y = 200
        xp = self.position_x
        yp = self.position_y

        # Ala principal (se reubica restando el centro)
        arcade.draw_polygon_filled([
            (300 + xp - center_x, 210 + yp - center_y),
            (260 + xp - center_x, 260 + yp - center_y),
            (340 + xp - center_x, 210 + yp - center_y)
        ], arcade.color.DARK_GRAY)

        # Fuselaje (elipse), centrado en (xp, yp)
        arcade.draw_ellipse_filled(300 + xp - center_x, 200 + yp - center_y, 200, 50, arcade.color.LIGHT_GRAY)
        # Cabina
        arcade.draw_ellipse_filled(360 + xp - center_x, 210 + yp - center_y, 40, 20, arcade.color.LIGHT_BLUE)
        # Nariz
        arcade.draw_triangle_filled(430 + xp - center_x, 200 + yp - center_y,
                                      380 + xp - center_x, 215 + yp - center_y,
                                      380 + xp - center_x, 185 + yp - center_y,
                                      arcade.color.LIGHT_GRAY)
        # Alerón vertical (cola)
        arcade.draw_triangle_filled(240 + xp - center_x, 200 + yp - center_y,
                                      200 + xp - center_x, 240 + yp - center_y,
                                      200 + xp - center_x, 200 + yp - center_y,
                                      arcade.color.LIGHT_GRAY)
        # Alerón horizontal (estabilizador trasero)
        arcade.draw_triangle_filled(220 + xp - center_x, 200 + yp - center_y,
                                      210 + xp - center_x, 190 + yp - center_y,
                                      210 + xp - center_x, 210 + yp - center_y,
                                      arcade.color.LIGHT_GRAY)
        # Otra ala, inferior
        arcade.draw_polygon_filled([
            (285 + xp - center_x, 200 + yp - center_y),
            (220 + xp - center_x, 160 + yp - center_y),
            (320 + xp - center_x, 200 + yp - center_y)
        ], arcade.color.DARK_GRAY)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        # Se oculta el puntero del ratón
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.ASH_GREY)
        # Se inicia el avión en el centro de la ventana
        self.plane = Plane(width // 2, height // 2)
        # Variables para almacenar los valores del joystick
        self.joystick = None
        self.joystick_x = 0
        self.joystick_y = 0

        # Se obtienen los joysticks conectados
        joysticks = arcade.get_joysticks()
        if joysticks:
            self.joystick = joysticks[0]
            self.joystick.open()
        else:
            print("There are no joysticks.")
            self.joystick = None

    def on_draw(self):
        self.clear()
        self.plane.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        # Actualiza la posición del avión para que el centro siga al ratón
        self.plane.position_x = x
        self.plane.position_y = y

    def on_joyaxis_motion(self, joystick, axis, value):
        # Se actualizan los valores del joystick
        # Eje 0: horizontal, Eje 1: vertical (pueden variar según el mando)
        if axis == 0:
            self.joystick_x = value
        elif axis == 1:
            self.joystick_y = value

    def on_update(self, delta_time):
        # Si se usa el joystick, se actualiza la posición del avión.
        if self.joystick:
            plane_speed = 200  # velocidad en píxeles por segundo
            self.plane.position_x += self.joystick_x * plane_speed * delta_time
            self.plane.position_y += self.joystick_y * plane_speed * delta_time

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Control de Avión: Ratón y Joystick")
    arcade.run()

if __name__ == "__main__":
    main()
