import arcade


class Heart(arcade.Sprite):
    def __init__(self,location):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.width=30
        self.height=30
        self.center_x=20+location*35
        self.center_y=20
        self.angle=330