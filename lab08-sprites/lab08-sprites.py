import random

import arcade
import pygame

SPRITE_SCALING_PLANE = 0.1
SPRITE_SCALING_CLOUD = 0.01
COUNT = 50

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


class Cloud(arcade.Sprite):
    """ This class manages a ball bouncing on the screen. """

    def __init__(self, image,scale,change_x, change_y):
        """ Constructor. """
        super().__init__(image, scale)

        # Take the parameters of the init function above, and create instance variables out of them.

        self.change_x = change_x
        self.change_y = change_y

    def update(self):
        """ Code to control the cloud's movement. """
        self.center_y += self.change_y
        self.center_x += self.change_x
        # Rebote en los bordes horizontales

        if self.left < 0 or self.right > SCREEN_WIDTH:
            self.change_x *= -1  # Invierte la dirección

            # Rebote en los bordes verticales
        if self.bottom < 0 or self.top > SCREEN_HEIGHT:
            self.change_y *= -1




class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        # Ocultamos el puntero del ratón.
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.ELECTRIC_BLUE)
        # Inicializamos el avión en el centro de la ventana.
        self.plane_sprite=None
        self.score=0
        self.plane_list=None
        self.cloud_list=None
        self.messaje=False

    def on_draw(self):
        self.clear()

        self.cloud_list.draw()
        self.plane_list.draw()
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        # Permite mover el avión con el ratón si se desea (aunque se puede comentar si se quiere solo joystick).
        self.plane_sprite.center_x = x
        self.plane_sprite.center_y = y

    def setup(self):
        self.plane_list=arcade.SpriteList()
        self.cloud_list=arcade.SpriteList()

        self.score=0

        self.plane_sprite=arcade.Sprite("plane.png", SPRITE_SCALING_PLANE)
        self.plane_sprite.center_x = 50
        self.plane_sprite.center_y = 50
        self.plane_list.append(self.plane_sprite)

        for i in range(COUNT):

            cloud = Cloud("cloud.png", SPRITE_SCALING_CLOUD,random.randrange(50),random.randrange(50))


            cloud.center_x = random.randrange(SCREEN_WIDTH-50)
            cloud.center_y = random.randrange(SCREEN_HEIGHT-50)


            self.cloud_list.append(cloud)

    def on_update(self, delta_time):
        # eventos de Pygame para actualizar el estado del joystick.
        pygame.event.pump()
        if joystick:
            # Se leen los ejes del joystick.
            x_axis = joystick.get_axis(0)
            y_axis = joystick.get_axis(1)
            plane_speed = 1000  # Velocidad en píxeles por segundo.
            # Actualizamos la posición del avión.
            self.plane_sprite.center_x += x_axis * plane_speed * delta_time
            # Normalmente el eje Y está invertido, así que usamos -y_axis.
            self.plane_sprite.center_y += -y_axis * plane_speed * delta_time

            while self.plane.center_x<-200:
                self.plane.center_x=1200
            while self.plane.center_x>1200:
                self.plane.center_x=-200
            while self.plane.center_y < -100:
                self.plane.center_y = 800
            while self.plane.center_y> 800:
                self.plane.center_y = -100

        self.cloud_list.on_update()

        self.cloud_list.update()
        clouds_hit_list = arcade.check_for_collision_with_list(self.plane_sprite,self.cloud_list)


        # Loop through each colliding sprite, remove it, and add to the score.
        for cloud in clouds_hit_list:
            cloud.remove_from_sprite_lists()
            self.score += 1
        if self.score==50:
            self.messaje=True



def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Avión controlado con Joystick (Pygame + Arcade)")
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
