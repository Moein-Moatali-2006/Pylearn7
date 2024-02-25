import arcade


class Board(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.center_x=x
        self.center_y=y
        self.width=85
        self.height=15
        self.speed=6
        self.change_x=0
        self.change_y=0
        self.score=0


    def move(self):
        self.center_x += self.change_x * self.speed

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,arcade.color.RED)

