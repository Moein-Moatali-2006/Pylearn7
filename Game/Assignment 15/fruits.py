import random
import arcade


class Fruit(arcade.Sprite):
    def __init__(self,game):
        super().__init__(game)
        # self.width=32
        # self.height=32
        # self.center_x=random.randint(15,game.width-15)
        # self.center_y=random.randint(15,game.height-15)
        # self.change_x=0
        # self.change_y=0


class Apple(Fruit):
    def __init__(self,game):
        super().__init__("pictures\Apple.png")
        self.width=32
        self.height=32
        self.center_x=random.randint(15,game.width-15)
        self.center_y=random.randint(15,game.height-15)
        self.change_x=0
        self.change_y=0


class Pear(Fruit):
    def __init__(self, game):
        super().__init__("pictures\Pear.png")
        self.width=32
        self.height=32
        self.center_x=random.randint(20,game.width-20)
        self.center_y=random.randint(20,game.height-20)
        self.change_x=0
        self.change_y=0


class PP(Fruit):
    def __init__(self, game):
        super().__init__("pictures\Shit.png")
        self.width=32
        self.height=32
        self.center_x=random.randint(15,game.width-15)
        self.center_y=random.randint(15,game.height-15)
        self.change_x=0
        self.change_y=0
        