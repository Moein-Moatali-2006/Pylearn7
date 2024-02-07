import arcade
from spaceship import SpaceShip
from enemy import Enemy


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=600,height=600,title="Moein Moatali")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.bg=arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me=SpaceShip(self.width,self.height)
        self.doshman=Enemy(self.width,self.height)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.bg)
        self.me.draw()
        self.doshman.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == 97:
            self.me.center_x -= self.me.speed
        elif symbol == 100:
            self.me.center_x += self.me.speed

    def on_update(self, delta_time: float):
        self.doshman.center_y -= self.doshman.speed